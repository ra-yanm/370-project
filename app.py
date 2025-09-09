from flask import Flask , redirect, request, make_response, render_template, flash , url_for, g
import mysql.connector
from flask_login import login_user, logout_user, login_required , current_user, LoginManager , UserMixin


app = Flask(__name__, template_folder='templates')
app.secret_key = "supersecret"


# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

#database connection
def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
                    host="localhost",
                    user="flaskBETA",        # DB user
                    password="beta223",      # DB password
                    database="notesflask"    # DB name
                    )
    return g.db

def get_cursor():
    if 'cursor' not in g:
        g.cursor = get_db().cursor(dictionary=True , buffered=True)  # dictionary=True is optional
    return g.cursor



@app.teardown_appcontext
def close_db(exception):
    cursor = g.pop('cursor', None)
    if cursor is not None:
        cursor.close()
    db = g.pop('db', None)
    if db is not None:
        db.close()




class User(UserMixin):
    def __init__(self, userid, user_type):
        self.userID = userid
        self.user_type = user_type

    def get_id(self):
        return str(self.userID)


@login_manager.user_loader
def load_user(userID):
    cursor = get_cursor()
    cursor.execute(f"SELECT user_ID, user_type FROM user WHERE user_ID = '{userID}'")
    row = cursor.fetchone()
    if row:
        return User(row['user_ID'], row['user_type'])
    return None


@app.route('/')
def frist_page():
    if  current_user.is_authenticated:
        return redirect('/home')
    else:
        return redirect('/login')


@app.errorhandler(404)  #for invalid urls redirecting them to home
def page_not_found(e):
    flash("404: Page not Found.")
    return redirect(url_for("home"))  




@app.route('/login', methods=['GET', 'POST'])
def login():
    if  current_user.is_authenticated:
        return redirect('/home')
    if request.method== 'GET':
        return render_template('login.html')
    elif request.method== 'POST':
        user_ID= request.form['userID']
        passw=request.form['password']
        cursor = get_cursor()

        try:
            if '@' in user_ID:
                cursor.execute(f"SELECT user_ID, user_type from user where email= '{str(user_ID)}' and password='{passw}'")
            else:
                cursor.execute(f"SELECT user_ID, user_type from user where user_ID= '{str(user_ID)}' and password='{passw}'")
        except:
            return redirect('/')
        row=cursor.fetchone()
        if row:
            user_obj=User(row['user_ID'], row['user_type'])
            login_user(user_obj)
            flash("Logged in successfully!")
            return redirect('/home')
        else:
            flash("Incorrect User ID or Password!")
            return redirect('/login')




@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect('/')



@app.route('/home')
@login_required
def home():
    try:
        cursor = get_cursor()

        cursor.execute(f"select name from user where user_ID='{current_user.userID}';")
        row=cursor.fetchone()
        return render_template('home.html', user_name=row['name'])
    except:
        return render_template('home.html')



def check_suggestion(noteID): #to check pending note suggestions
    try:
        cursor = get_cursor()

        cursor.execute(f"SELECT noteID FROM note_suggestions WHERE noteID='{noteID}';")
        have_suggestion= cursor.fetchone()
        if have_suggestion:
            return True
        else:
            return False
    except:
        return False
app.jinja_env.globals.update(check_suggestion=check_suggestion) #Registering the function as a global


def check_pending_note(courseID): #to check pending note posts
    try:
        cursor = get_cursor()

        cursor.execute(f"SELECT courseID FROM note_pending WHERE courseID='{courseID}' GROUP BY courseID;")
        have_pending = cursor.fetchone()
        if have_pending:
            return True
        else:
            return False
    except:
        return False
app.jinja_env.globals.update(check_pending_note=check_pending_note) #Registering the function as a global



import difflib

# ... other imports and Flask app setup

def highlight_diff(original_text, new_text):
    """
    Compares two strings and returns an HTML string with added and deleted
    words highlighted.
    """
    # Split the strings into words for comparison
    original_words = original_text.split()
    new_words = new_text.split()

    # Create a sequence matcher object
    matcher = difflib.SequenceMatcher(None, original_words, new_words)

    highlighted_html = ""
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            highlighted_html += ' '.join(original_words[i1:i2]) + " "
        elif tag == 'delete':
            highlighted_html += f'<span class="deleted">{" ".join(original_words[i1:i2])}</span> '
        elif tag == 'insert':
            highlighted_html += f'<span class="added">{" ".join(new_words[j1:j2])}</span> '
        elif tag == 'replace':
            highlighted_html += f'<span class="deleted">{" ".join(original_words[i1:i2])}</span> '
            highlighted_html += f'<span class="added">{" ".join(new_words[j1:j2])}</span> '
            
    return highlighted_html.strip()

app.jinja_env.globals.update(highlight_diff=highlight_diff) #Registering the function as a global

@app.route('/notes',  methods=['GET', 'POST'])
@login_required
def viewnote():
    try:
        cursor = get_cursor()
        #shows a specified note
        if 'course' in request.args.keys() and 'L' in request.args.keys():
            cursor.execute(f"SELECT note,title, student_view FROM notes WHERE noteID='{request.args['L']}';")
            notes = cursor.fetchone()            
            have_suggestion= check_suggestion(request.args['L'])
            return render_template("note.html", notes=notes, have_suggestion=have_suggestion, course=request.args['course'], noteID=request.args['L'])    
        #shows all notes in a specified course and the course details 
        elif 'course' in request.args.keys() and 'L' not in request.args.keys():
            cursor.execute(f"SELECT courseID, title, description from courses WHERE courseID='{request.args['course']}'")
            course_info=cursor.fetchone()
            if not course_info:
                return redirect("/notes")
            cursor.execute(f"SELECT courseID, noteID, title, student_view FROM notes WHERE courseID='{request.args['course']}' order by noteID")
            notes=cursor.fetchall()
            return render_template("all_note.html", notes=notes , course_info=course_info, course=request.args['course'])
        #shows all courses in databse
        else:
            cursor.execute(f"SELECT courseID FROM courses order by courseID")
            courses=cursor.fetchall()
            return render_template("all_note.html", courses=courses)
    
    except mysql.connector.Error as err:
            flash(f"Error: {err.msg}")
            return redirect(f"/notes")





@app.route('/submit_suggestion', methods=['POST'])
@login_required
def submit_suggestion(): #to submit suggestion for a specific note
    course = request.form['course']
    noteID = request.form['noteID']
    suggestion_note = request.form['suggestion_note']
    buttton=request.form['buttton']
    cursor = get_cursor()
    db = get_db()

    cursor.execute(f"SELECT note FROM notes WHERE noteID='{noteID}';")
    notes = cursor.fetchone()
    if notes['note']==suggestion_note or suggestion_note=='':
        flash("No changes, [Not submitted]")
    else:
        try :
            if buttton=='suggesting':
                cursor.execute(f"INSERT INTO note_suggestions (courseID, noteID, suggestion, suggested_by) VALUES ('{course}', '{noteID}', '{suggestion_note}', '{current_user.userID}');")
                db.commit()
                flash("Suggestion submitted!")
            elif buttton=='saving':
                cursor.execute(f"UPDATE notes SET note = '{suggestion_note}' WHERE noteID = '{noteID}';")
                db.commit()
                flash("Saved!")
        except mysql.connector.Error as err:
            flash(f"Error: {err.msg}")
    return redirect(f"/notes?course={course}&L={noteID}")



@app.route('/hide_note', methods=['POST'])
@login_required
def hide_the_note(): #to hide/unhide a specific note
    if current_user.user_type=='faculty':
        course = request.form['course']
        noteID = request.form['noteID']
        student_view = request.form['hide']
        cursor = get_cursor()
        db = get_db()

        if  student_view=='1':
            try:
                cursor.execute(f"UPDATE notes SET student_view = '{student_view}' WHERE noteID = '{noteID}';")
                db.commit()
                flash("Status Updated! [Now Unhidden]")
            except mysql.connector.Error as err:
                flash(f"Error: {err.msg}")
        elif student_view=='0':
            try:
                cursor.execute(f"UPDATE notes SET student_view = '{student_view}' WHERE noteID = '{noteID}';")
                db.commit()
                flash("Status Updated! [Now Hidden]")
            except mysql.connector.Error as err:
                flash(f"Error: {err.msg}")
    return redirect(f"/notes?course={course}&L={noteID}")



@app.route('/deleting', methods=['POST','GET'])
@login_required
def delete_the_note(): #to delete a specific note/course
    if current_user.user_type!='faculty':
        flash('Access denied.')
        redirect(f"/notes")
    if request.method == "GET": #r u sure page before deleting
            if 'L' in request.args.keys():
                cursor = get_cursor()
                db = get_db()
                cursor.execute(f"SELECT courseID,title FROM notes WHERE noteID='{request.args['L']}';")
                notes = cursor.fetchone()     
                return render_template('delete_cn.html' , note=notes, lec=request.args['L'])
            elif 'course' in request.args.keys():
                cursor = get_cursor()
                db = get_db()
                cursor.execute(f"SELECT courseID, title FROM courses WHERE courseID='{request.args['course']}';")
                course_info = cursor.fetchone()   
                return render_template('delete_cn.html' ,course_info=course_info, course=request.args['course'])
            else:
                redirect(f"/notes")

    if request.method == "POST": #actual deletation
        buttton=request.form['buttton']
        if buttton=='lec':
            noteID = request.form['noteID']
            courseID = request.form['courseID']
            cursor = get_cursor()
            db = get_db()
            try:
                cursor.execute(f"DELETE FROM notes WHERE noteID = '{noteID}';")
                cursor.execute(f"DELETE FROM note_suggestions WHERE noteID = '{noteID}';")
                db.commit()
                flash("[Note Deleted]")
            except mysql.connector.Error as err:
                flash(f"Error: {err.msg}")
            return redirect(f"/notes?course={courseID}")
        elif  buttton=='course_':
            courseID = request.form['courseID']
            cursor = get_cursor()
            db = get_db()
            try:
                cursor.execute(f"DELETE FROM courses WHERE courseID = '{courseID}';")
                db.commit()
                flash("[Course Deleted]")
            except mysql.connector.Error as err:
                flash(f"Error: {err.msg}")
    return redirect(f"/notes")



@app.route('/add_note', methods=['GET', 'POST'])
@login_required
def add_note():  #adding new notes under a selected course available
    if current_user.user_type == 'alumni':
        flash('Access denied.')
        return redirect('/notes')
    if request.method == 'POST':
        courseID=request.form['courseID']
        title=request.form['title']
        note=request.form['note']
        cursor = get_cursor()
        db = get_db()

        try:
            if current_user.user_type=='faculty':
                if 'student_view' in request.form:
                    student_view=request.form['student_view']
                else:
                    student_view='0'
                cursor.execute(f"INSERT INTO notes (courseID, title, note, student_view) VALUES ('{courseID}', '{title}', '{note}', '{student_view}');")
                db.commit()
                flash('Note added successfully!')
                return redirect(f'/notes?course={courseID}')
            else:
                cursor.execute(f"INSERT INTO note_pending (courseID, title, note, post_by) VALUES ('{courseID}', '{title}', '{note}', '{current_user.userID}');")
                db.commit()
                flash('Note has been submitted for approval.')
                return redirect(f'/notes?course={courseID}')
        except mysql.connector.Error as err:
            flash(f"Error: {err.msg}")
            return redirect('/add_note')
    else:
        cursor = get_cursor()
        cursor.execute(f"SELECT courseID FROM courses ORDER BY courseID;")
        courses=cursor.fetchall()
        return render_template('add_note.html', courses=courses)



@app.route('/approve_suggestion', methods=["GET", "POST"])
@login_required
def approve_suggestion():    #for st/faculty to approve suggestions on a specific note
    if current_user.user_type == 'faculty' or current_user.user_type == 'st':
        if request.method == "GET":
            try:
                cursor = get_cursor()

                if 'L' in request.args.keys():
                    # Fetch original note details
                    cursor.execute(f"SELECT note, title, courseID FROM notes WHERE noteID='{request.args['L']}'")
                    note = cursor.fetchone()
                    
                    if not note:
                        flash("Note not found.")
                        return redirect("/notes")

                    # Fetch all suggestions for this note
                    cursor.execute(f"SELECT suggestion, suggested_by, suggestionID FROM note_suggestions WHERE noteID='{request.args['L']}';")
                    suggestions = cursor.fetchall()
                    
                    # Process each suggestion to highlight differences
                    highlighted_suggestions = []
                    for suggestion in suggestions:
                        original_note = note['note']
                        suggested_note_text = suggestion['suggestion']
                        
                        # Use the helper function to get the highlighted HTML
                        highlighted_html = highlight_diff(original_note, suggested_note_text)
                        
                        # Add the highlighted text to the suggestion dictionary
                        suggestion['highlighted_html'] = highlighted_html
                        highlighted_suggestions.append(suggestion)

                    return render_template(
                        "suggestions.html", 
                        notes=note, 
                        course=note['courseID'], 
                        noteID=request.args['L'], 
                        suggestions=highlighted_suggestions
                    )
            except mysql.connector.Error as err:
                flash(f"Error: {err.msg}")
                return redirect("/notes")

        # Handle POST requests for approval/rejection
        if request.method == "POST":
            noteID = request.form.get('noteID')
            suggestID = request.form.get('suggestionID')
            courseID = request.form.get('courseID')
            buttton = request.form.get('buttton')
            
            cursor = get_cursor()
            db = get_db()

            try:
                if buttton == 'approve':
                    suggestion_text = request.form.get('suggestion')
                    cursor.execute(f"UPDATE notes SET note = '{suggestion_text}' WHERE noteID = '{noteID}';")
                    cursor.execute(f"DELETE FROM note_suggestions WHERE suggestionID = '{suggestID}';")
                    db.commit()
                    flash("Note Updated!")
                elif buttton == 'reject':
                    cursor.execute(f"DELETE FROM note_suggestions WHERE suggestionID = '{suggestID}';")
                    db.commit()
                    flash("Suggestion Deleted.")
            except mysql.connector.Error as err:
                flash(f"Error: {err.msg}")
            
            return redirect(f"/notes?course={courseID}&L={noteID}")
    
    else:
        flash("No permission to access this page.")
        return redirect(request.referrer or "/notes")


@app.route('/add_course', methods=["GET" , "POST"])
@login_required
def adding_course(): #for a faculty to add a new course
    if current_user.user_type!='faculty':
         return redirect('/notes')
    if request.method=='GET':
        return render_template('add_course.html')
    else:
        courseid=request.form['courseID'].upper()
        title=request.form['title']
        descriptions=request.form['descriptons']
        cursor = get_cursor()
        db = get_db()

        try:
            cursor.execute(f"INSERT INTO courses (courseID, title, description) VALUES ('{courseid}','{title}','{descriptions}');")
            db.commit()
            flash('Course added successfully!')
            return redirect('/notes')
        except mysql.connector.Error as err:
            flash(f"Error: {err.msg}")
        return redirect(f"/add_course")






@app.route('/approve_note', methods=["GET", "POST"])
@login_required
def approve_note(): #for a faculty to approve new notes under a course
    if current_user.user_type=='faculty':
        if request.method=="GET":
            cursor = get_cursor()

            if 'course' in request.args.keys():
                cursor.execute(f"SELECT note, title, post_by, ID FROM note_pending WHERE courseID='{request.args['course']}';")
                suggestions=cursor.fetchall()
                return render_template("approve_notes.html", course=request.args['course'] , suggestions=suggestions)
        pending_ID=request.form['pending_ID']
        courseID=request.form['courseID']
        buttton=request.form['buttton']
        cursor = get_cursor()
        db = get_db()

        try:
            if buttton=='approve':
                note=request.form['note']
                title=request.form['title']
                cursor.execute(f"INSERT INTO notes (courseID, title, note, student_view) VALUES ('{courseID}', '{title}', '{note}', '1');")
                cursor.execute(f"DELETE FROM note_pending WHERE ID = '{pending_ID}';")
                db.commit()
                flash("Note Added!")
            elif buttton=='reject':
                cursor.execute(f"DELETE FROM note_pending WHERE ID = '{pending_ID}';")
                db.commit()
                flash("[Deleted]")
        except mysql.connector.Error as err:
            flash(f"Error: {err.msg}")
        return redirect(f"/notes?course={courseID}")
    else:
        flash(f"No permission to access this page.")
        return redirect(f"/notes")



#####ramisa's part

@app.route('/requests')
@login_required
def requests():
    cursor = get_cursor()
    try:
        cursor.execute("""
            SELECT u.name, s.cgpa
            FROM user u
            LEFT JOIN student s ON u.user_ID = s.user_ID
            WHERE u.user_ID=%s
        """, (current_user.userID,))
        row = cursor.fetchone()
        user_name = row['name'] if row else "User"
        cgpa = row['cgpa'] if row and row['cgpa'] is not None else "N/A"
        return render_template('requests.html', user_name=user_name, cgpa=cgpa)
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}")
        return render_template('requests.html', user_name="User", cgpa="N/A")

# --- Section swap ---
@app.route('/section_swap', methods=['GET', 'POST'])
@login_required
def section_swap():
    cursor = get_cursor()
    search_query = None

    if request.method == 'POST':
        search_query = request.form.get("search")
    if search_query:
        cursor.execute("""
            SELECT ss.id, u.name, u.user_ID, s.cgpa, ss.course_code, 
                   ss.current_section, ss.desired_section, ss.status
            FROM section_swap ss
            JOIN user u ON ss.student_id = u.user_ID
            LEFT JOIN student s ON u.user_ID = s.user_ID
            WHERE ss.status = 'pending' AND ss.course_code LIKE %s
        """, (f"%{search_query}%",))
    else:
        cursor.execute("""
            SELECT ss.id, u.name, u.user_ID, s.cgpa, ss.course_code, ss.current_section, ss.desired_section, ss.status
            FROM section_swap ss
            JOIN user u ON ss.student_id = u.user_ID
            LEFT JOIN student s ON u.user_ID = s.user_ID
            WHERE ss.status = 'pending'
            AND ss.id NOT IN (
                SELECT request_id 
                FROM ignored_requests 
                WHERE user_id=%s AND request_type='section'
            )
        """, (current_user.userID,))
    requests = cursor.fetchall()
    return render_template(
        'section_swap.html',
        requests=requests,
        logged_in_user_id=current_user.userID,
        search_query=search_query or ""
    )  

@app.route('/make_section_request', methods=['GET', 'POST'])
@login_required
def make_section_request():
    cursor = get_cursor()
    if request.method == 'POST':
        student_id = current_user.userID
        course_code = request.form['course_code']
        current_section = request.form['current_section']
        desired_section = request.form['desired_section']
        try:
            cursor.execute("""
                INSERT INTO section_swap (student_id, course_code, current_section, desired_section)
                VALUES (%s,%s,%s,%s)
            """, (student_id, course_code, current_section, desired_section))
            get_db().commit()
            flash("Section request submitted successfully!")
        except mysql.connector.Error as err:
            flash(f"Error: {err.msg}")
        return redirect(url_for('section_swap'))
    return render_template('make_section_request.html')

@app.route('/section_swap/update/<int:req_id>/<string:action>')
@login_required
def update_section_request(req_id, action):
    cursor = get_cursor()
    try:
        cursor.execute("SELECT student_id, status FROM section_swap WHERE id=%s", (req_id,))
        req = cursor.fetchone()
        if not req:
            flash("Section swap request not found.", "danger")
            return redirect(url_for('section_swap'))
        if str(req['student_id']) == str(current_user.userID):
            flash("You cannot accept or reject your own request.", "warning")
            return redirect(url_for('section_swap'))
        if req['status'] != 'pending':
            flash(f"This request has already been {req['status']}.", "info")
            return redirect(url_for('section_swap'))

        if action.lower() == 'accepted':
            cursor.execute("UPDATE section_swap SET status='accepted' WHERE id=%s", (req_id,))
            get_db().commit()
            flash("Request accepted successfully!", "success")
        elif action.lower() == 'rejected':
            cursor.execute("UPDATE section_swap SET status='rejected' WHERE id=%s", (req_id,))
            get_db().commit()
            flash("Request rejected successfully!", "info")
        else:
            flash("Invalid action.", "danger")
    except mysql.connector.Error as err:
        flash(f"Error updating request: {err.msg}", "danger")

    return redirect(url_for('section_swap'))

# --- Thesis group ---
@app.route('/find_thesisgroup', methods=['GET', 'POST'])
@login_required
def find_thesisgroup():
    cursor = get_cursor()
    search_query = None

    if request.method == 'POST':
        search_query = request.form.get("search", "").strip()

    if search_query:
        cursor.execute("""
            SELECT ft.id, u.name, u.email, s.cgpa, ft.topic, ft.research_area, ft.group_id, ft.members_needed,
                   ft.student_id, ft.status
            FROM find_thesisgroup ft
            JOIN user u ON ft.student_id = u.user_ID
            LEFT JOIN student s ON u.user_ID = s.user_ID
            WHERE ft.status = 'pending'
              AND (ft.topic LIKE %s OR ft.research_area LIKE %s)
        """, (f"%{search_query}%", f"%{search_query}%"))
    else:
        cursor.execute("""
            SELECT ft.id, u.name, u.email, s.cgpa, ft.topic, ft.research_area, ft.group_id, ft.members_needed,
                   ft.student_id, ft.status
            FROM find_thesisgroup ft
            JOIN user u ON ft.student_id = u.user_ID
            LEFT JOIN student s ON u.user_ID = s.user_ID
            WHERE ft.status = 'pending'
              AND ft.id NOT IN (
                SELECT request_id 
                FROM ignored_requests 
                WHERE user_id=%s AND request_type='thesis'
              )
        """, (current_user.userID,))

    requests = cursor.fetchall()

    return render_template(
        'thesis_group.html',
        requests=requests,
        logged_in_user_id=current_user.userID,
        user_actions={}, 
        search_query=search_query or ""
    )

@app.route('/make_thesis_request', methods=['GET', 'POST'])
@login_required
def make_thesis_request():
    cursor = get_cursor()
    if request.method == 'POST':
        topic = request.form['topic']
        research_area = request.form['research_area']
        members_needed = request.form['members_needed']
        group_id = request.form['group_id']

        try:
            cursor.execute("SELECT id FROM find_thesisgroup WHERE group_id=%s", (group_id,))
            existing = cursor.fetchone()
            if existing:
                flash(f"Group ID '{group_id}' already exists. Please choose a different Group ID.", "danger")
                return redirect(url_for('make_thesis_request'))

            cursor.execute("""
                INSERT INTO find_thesisgroup (student_id, topic, research_area, members_needed, group_id, status)
                VALUES (%s, %s, %s, %s, %s, 'pending')
            """, (current_user.userID, topic, research_area, members_needed, group_id))
            get_db().commit()
            flash("Thesis request created successfully.", "success")
        except mysql.connector.Error as err:
            flash(f"Error: {err.msg}")
        return redirect(url_for('find_thesisgroup'))
    return render_template('make_thesis_request.html')

@app.route('/find_thesisgroup/update/<int:req_id>/<string:action>')
@login_required
def update_thesis_request(req_id, action):
    cursor = get_cursor()
    try:
        cursor.execute("SELECT student_id, status FROM find_thesisgroup WHERE id=%s", (req_id,))
        req = cursor.fetchone()

        if not req:
            flash("Thesis request not found.", "danger")
            return redirect(url_for('find_thesisgroup'))

        if str(req['student_id']) == str(current_user.userID):
            flash("You cannot accept or reject your own request.", "warning")
            return redirect(url_for('find_thesisgroup'))

        if req['status'] != 'pending':
            flash(f"This request has already been {req['status']}.", "info")
            return redirect(url_for('find_thesisgroup'))

        if action.lower() == 'accepted':
            cursor.execute("UPDATE find_thesisgroup SET status='accepted' WHERE id=%s", (req_id,))
            get_db().commit()
            flash("Thesis request accepted!", "success")

            cursor.execute("SELECT topic, research_area FROM find_thesisgroup WHERE id=%s", (req_id,))
            thesis = cursor.fetchone()
            if thesis:
                message = f"Your thesis request has been accepted!\nThesis Topic: {thesis['topic']}\nResearch Area: {thesis['research_area']}"
                cursor.execute("""
                    INSERT INTO accepted_invitations (sender_id, receiver_id, message)
                    VALUES (%s, %s, %s)
                """, (current_user.userID, req['student_id'], message))
                get_db().commit()
        elif action.lower() == 'rejected':
            cursor.execute("UPDATE find_thesisgroup SET status='rejected' WHERE id=%s", (req_id,))
            get_db().commit()
            flash("Thesis request rejected.", "info")
        else:
            flash("Invalid action.", "danger")
    except mysql.connector.Error as err:
        flash(f"Error updating request: {err.msg}", "danger")

    return redirect(url_for('find_thesisgroup'))

# --- Accepted invitations ---
@app.route('/accepted_invitations')
@login_required
def view_accepted_invitations():
    cursor = get_cursor()
    try:
        cursor.execute("""
            SELECT ai.id, u.user_ID AS sender_id, u.name AS sender_name,
                   u.email AS sender_email, s.cgpa, ai.message
            FROM accepted_invitations ai
            JOIN user u ON ai.sender_id = u.user_ID
            LEFT JOIN student s ON u.user_ID = s.user_ID
            WHERE ai.receiver_id = %s
        """, (current_user.userID,))
        invitations = cursor.fetchall()
        return render_template('accepted_invitations.html', invitations=invitations)
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}")
        return redirect('/home')

@app.route('/accepted_invitations/delete/<int:inv_id>', methods=['POST'])
@login_required
def delete_invitation(inv_id):
    cursor = get_cursor()
    try:
        cursor.execute("SELECT * FROM accepted_invitations WHERE id=%s AND receiver_id=%s",
                       (inv_id, current_user.userID))
        inv = cursor.fetchone()
        if not inv:
            flash("Invitation not found or unauthorized.", "warning")
            return redirect(url_for('view_accepted_invitations'))

        cursor.execute("DELETE FROM accepted_invitations WHERE id=%s", (inv_id,))
        get_db().commit()
        flash("Notification deleted successfully.", "success")
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}")
    return redirect(url_for('view_accepted_invitations'))

# --- My active requests ---
@app.route("/my_active_requests")
@login_required
def my_active_requests():
    cursor = get_cursor()
    try:
        user_id = current_user.userID
        cursor.execute("""
            SELECT id, topic, research_area, group_id, members_needed, status
            FROM find_thesisgroup
            WHERE student_id = %s AND status = 'pending'
        """, (user_id,))
        requests = cursor.fetchall()

        cursor.execute("""
            SELECT id, course_code, current_section, desired_section, status
            FROM section_swap
            WHERE student_id = %s AND status = 'pending'
        """, (user_id,))
        section_reqs = cursor.fetchall()

        return render_template("my_active_requests.html", requests=requests, section_requests=section_reqs)
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}")
        return redirect('/home')

@app.route("/delete_request/<string:table>/<int:req_id>", methods=["POST"])
@login_required
def delete_request(table, req_id):
    cursor = get_cursor()
    try:
        user_id = current_user.userID
        if table == "thesis":
            cursor.execute("DELETE FROM find_thesisgroup WHERE id=%s AND student_id=%s", (req_id, user_id))
        elif table == "section":
            cursor.execute("DELETE FROM section_swap WHERE id=%s AND student_id=%s", (req_id, user_id))
        else:
            flash("Invalid request type", "danger")
            return redirect(url_for("my_active_requests"))
        get_db().commit()
        flash("Request deleted successfully.", "success")
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}")
    return redirect(url_for("my_active_requests"))

@app.route('/ignored_requests')
@login_required
def ignored_requests():
    cursor = get_cursor()
    try:
        cursor.execute("""
            SELECT ir.id AS ignored_id, ir.request_type, ir.request_id, ir.ignored_at,
                   f.id AS thesis_id, f.topic, f.research_area, f.group_id,
                   s.id AS section_id, s.course_code, s.current_section, s.desired_section, s.status
            FROM ignored_requests ir
            LEFT JOIN find_thesisgroup f ON ir.request_type='thesis' AND ir.request_id=f.id
            LEFT JOIN section_swap s ON ir.request_type='section' AND ir.request_id=s.id
            WHERE ir.user_id = %s
            ORDER BY ir.ignored_at DESC
        """, (current_user.userID,))
        ignored = cursor.fetchall()
        return render_template("ignored_requests.html", ignored=ignored)
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}")
        return redirect('/home')

@app.route('/ignore_request/<string:table>/<int:req_id>', methods=['POST'])
@login_required
def ignore_request(table, req_id):
    cursor = get_cursor()
    try:
    
        cursor.execute("SELECT * FROM ignored_requests WHERE user_id=%s AND request_type=%s AND request_id=%s",
                       (current_user.userID, table, req_id))
        existing = cursor.fetchone()
        if existing:
            flash("This request is already ignored.", "warning")
            return redirect(url_for('ignored_requests'))

      
        cursor.execute("""
            INSERT INTO ignored_requests (user_id, request_type, request_id, ignored_at)
            VALUES (%s, %s, %s, NOW())
        """, (current_user.userID, table, req_id))
        get_db().commit()
        flash("Request ignored successfully.", "success")
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}", "danger")
    return redirect(url_for('ignored_requests'))

@app.route('/ignored_requests/accept/thesis/<int:req_id>')
@login_required
def accept_ignored_thesis(req_id):
    cursor = get_cursor()
    try:
        cursor.execute("DELETE FROM ignored_requests WHERE user_id=%s AND request_type='thesis' AND request_id=%s",
                       (current_user.userID, req_id))
        get_db().commit()
        return redirect(url_for('update_thesis_request', req_id=req_id, action="accepted"))
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}", "danger")
        return redirect(url_for('ignored_requests'))

@app.route('/ignored_requests/accept/section/<int:req_id>')
@login_required
def accept_ignored_section(req_id):
    cursor = get_cursor()
    try:
        cursor.execute("SELECT status FROM section_swap WHERE id=%s", (req_id,))
        req = cursor.fetchone()
        if not req or req['status'] == 'accepted':
            flash("This section swap has already been accepted by someone else.", "warning")
            return redirect(url_for('ignored_requests'))

        cursor.execute("DELETE FROM ignored_requests WHERE user_id=%s AND request_type='section' AND request_id=%s",
                       (current_user.userID, req_id))
        get_db().commit()
        return redirect(url_for('update_section_request', req_id=req_id, action="accepted"))
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}", "danger")
        return redirect(url_for('ignored_requests'))

@app.route('/ignored_requests/delete/<int:req_id>', methods=['POST'])
@login_required
def delete_ignored_request(req_id):
    cursor = get_cursor()
    try:
        cursor.execute("SELECT * FROM ignored_requests WHERE id=%s AND user_id=%s", 
                       (req_id, current_user.userID))
        ignored = cursor.fetchone()
        if not ignored:
            flash("Ignored request not found or unauthorized.", "warning")
            return redirect(url_for('ignored_requests'))

        cursor.execute("DELETE FROM ignored_requests WHERE id=%s", (req_id,))
        get_db().commit()
        flash("Ignored request deleted successfully.", "success")
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}", "danger")
    return redirect(url_for('ignored_requests'))


#---mishu part---
@app.route('/notices')
@login_required
def view_notices():
    try:
        cursor = get_cursor()
        cursor.execute(f"""
            SELECT n.*, u.name as posted_by_name
            FROM Notice n
            JOIN user u ON n.posted_by = u.user_ID
            ORDER BY n.notice_id DESC
        """)
        notices = cursor.fetchall()
        return render_template('notices.html', notices=notices)
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}")
        return redirect('/home')

@app.route('/post_notice', methods=['GET', 'POST'])
@login_required
def post_notice():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        notice_type = request.form['type']
        posted_by = current_user.userID
        
        cursor = get_cursor()
        db = get_db()
        
        try:
            cursor.execute(f"""
                INSERT INTO Notice (title, description, type, posted_by) 
                VALUES ('{title}', '{description}', '{notice_type}', '{posted_by}')
            """)

            db.commit()
            flash('Notice posted successfully!')
            return redirect('/notices')
        except mysql.connector.Error as err:
            flash(f"Error: {err.msg}")
            return redirect('/post_notice')
    
    return render_template('post_notice.html')

@app.route('/edit_notice/<int:notice_id>', methods=['GET', 'POST'])
@login_required
def edit_notice(notice_id):
    cursor = get_cursor()
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        notice_type = request.form['type']
        
        db = get_db()
        
        try:
            # Check if the notice belongs to the current user
            cursor.execute(f"SELECT posted_by FROM Notice WHERE notice_id = '{notice_id}'")
            notice = cursor.fetchone()
            
            if not notice or notice['posted_by'] != current_user.userID:
                flash('You can only edit your own notices.')
                return redirect('/notices')
            
            cursor.execute(f"""
                UPDATE Notice 
                SET title = '{title}', description = '{description}', type = '{notice_type}'
                WHERE notice_id = '{notice_id}'
            """)
            db.commit()
            flash('Notice updated successfully!')
            return redirect('/notices')
        except mysql.connector.Error as err:
            flash(f"Error: {err.msg}")
            return redirect(f'/edit_notice/{notice_id}')
    
    try:
        cursor.execute(f"SELECT * FROM Notice WHERE notice_id = '{notice_id}'")
        notice = cursor.fetchone()
        
        if not notice or notice['posted_by'] != current_user.userID:
            flash('You can only edit your own notices.')
            return redirect('/notices')
        
        return render_template('edit_notice.html', notice=notice)
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}")
        return redirect('/notices')

@app.route('/delete_notice/<int:notice_id>', methods=['POST'])
@login_required
def delete_notice(notice_id):
    cursor = get_cursor()
    db = get_db()
    
    try:
        # Check if the notice belongs to the current user
        cursor.execute(f"SELECT posted_by FROM Notice WHERE notice_id = '{notice_id}'")
        notice = cursor.fetchone()
        
        if not notice or notice['posted_by'] != current_user.userID:
            flash('You can only delete your own notices.')
            return redirect('/notices')
        
        cursor.execute(f"DELETE FROM Notice WHERE notice_id = '{notice_id}'")
        db.commit()
        flash('Notice deleted successfully!')
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}")
    
    return redirect('/notices')

@app.route('/notice_details/<int:notice_id>')
@login_required
def notice_details(notice_id):
    try:
        cursor = get_cursor()
        cursor.execute(f"""
            SELECT n.*, u.name as posted_by_name
            FROM Notice n
            JOIN user u ON n.posted_by = u.user_ID
            WHERE n.notice_id = '{notice_id}'
        """)
        notice = cursor.fetchone()
        
        if not notice:
            flash('Notice not found.')
            return redirect('/notices')
        
        return render_template('notice_details.html', notice=notice)
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}")
        return redirect('/notices')
#notice added

#alumni 
@app.route('/alumni_meetups')
@login_required
def view_meetups():
    # Only alumni can view meetups
    if current_user.user_type != 'alumni':
        flash('Only alumni can access this page.')
        return redirect('/home')
    
    try:
        cursor = get_cursor()
        cursor.execute(f"""
            SELECT a.*, u.name as arranged_by_name
            FROM Alumni a
            JOIN user u ON a.Arranged_by = u.user_ID
            ORDER BY a.Date ASC
        """)
        meetups = cursor.fetchall()
        return render_template('alumni_meetups.html', meetups=meetups)
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}")
        return redirect('/home')

@app.route('/add_meetup', methods=['GET', 'POST'])
@login_required
def add_meetup():
    # Only alumni can arrange meetups
    if current_user.user_type != 'alumni':
        flash('Only alumni can arrange meetups.')
        return redirect('/home')
    
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        location = request.form['location']
        batch = request.form['batch']
        arranged_by = current_user.userID
        
        cursor = get_cursor()
        db = get_db()
        
        try:
            cursor.execute(f"""
                INSERT INTO Alumni (Title, Date, Location, Batch, Arranged_by) 
                VALUES ('{title}', '{date}', '{location}', '{batch}', '{arranged_by}')
            """)
            db.commit()
            flash('Meetup arranged successfully!')
            return redirect('/alumni_meetups')
        except mysql.connector.Error as err:
            flash(f"Error: {err.msg}")
            return redirect('/add_meetup')
    
    return render_template('add_meetup.html')

@app.route('/edit_meetup/<int:meetup_id>', methods=['GET', 'POST'])
@login_required
def edit_meetup(meetup_id):
    # Only alumni can edit meetups
    if current_user.user_type != 'alumni':
        flash('Only alumni can edit meetups.')
        return redirect('/home')
    
    cursor = get_cursor()
    
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        location = request.form['location']
        batch = request.form['batch']
        
        db = get_db()
        
        try:
            # Check if the meetup belongs to the current user
            cursor.execute(f"SELECT Arranged_by FROM Alumni WHERE EvenID = '{meetup_id}'")
            meetup = cursor.fetchone()
            
            if not meetup or meetup['Arranged_by'] != current_user.userID:
                flash('You can only edit your own meetups.')
                return redirect('/alumni_meetups')
            
            cursor.execute(f"""
                UPDATE Alumni 
                SET Title = '{title}', Date = '{date}', Location = '{location}', Batch = '{batch}'
                WHERE EvenID = '{meetup_id}'
            """)
            db.commit()
            flash('Meetup updated successfully!')
            return redirect('/alumni_meetups')
        except mysql.connector.Error as err:
            flash(f"Error: {err.msg}")
            return redirect(f'/edit_meetup/{meetup_id}')
    
    try:
        cursor.execute(f"SELECT * FROM Alumni WHERE EvenID = '{meetup_id}'")
        meetup = cursor.fetchone()
        
        if not meetup or meetup['Arranged_by'] != current_user.userID:
            flash('You can only edit your own meetups.')
            return redirect('/alumni_meetups')
        
        return render_template('edit_meetup.html', meetup=meetup)
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}")
        return redirect('/alumni_meetups')

@app.route('/delete_meetup/<int:meetup_id>', methods=['POST'])
@login_required
def delete_meetup(meetup_id):
    # Only alumni can delete meetups
    if current_user.user_type != 'alumni':
        flash('Only alumni can delete meetups.')
        return redirect('/home')
    
    cursor = get_cursor()
    db = get_db()
    
    try:
        # Check if the meetup belongs to the current user
        cursor.execute(f"SELECT Arranged_by FROM Alumni WHERE EvenID = '{meetup_id}'")
        meetup = cursor.fetchone()
        
        if not meetup or meetup['Arranged_by'] != current_user.userID:
            flash('You can only delete your own meetups.')
            return redirect('/alumni_meetups')
        
        cursor.execute(f"DELETE FROM Alumni WHERE EvenID = '{meetup_id}'")
        db.commit()
        flash('Meetup deleted successfully!')
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}")
    
    return redirect('/alumni_meetups')

@app.route('/meetup_details/<int:meetup_id>')
@login_required
def meetup_details(meetup_id):
    # Only alumni can view meetup details
    if current_user.user_type != 'alumni':
        flash('Only alumni can access this page.')
        return redirect('/home')
    
    try:
        cursor = get_cursor()
        cursor.execute(f"""
            SELECT a.*, u.name as arranged_by_name
            FROM Alumni a
            JOIN user u ON a.Arranged_by = u.user_ID
            WHERE a.EvenID = '{meetup_id}'
        """)
        meetup = cursor.fetchone()
        
        if not meetup:
            flash('Meetup not found.')
            return redirect('/alumni_meetups')
        
        return render_template('meetup_details.html', meetup=meetup)
    except mysql.connector.Error as err:
        flash(f"Error: {err.msg}")
        return redirect('/alumni_meetups')
    
if __name__=="__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)