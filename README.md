# CampusLink

CampusLink is a Flask-based web application designed for university students, faculty, and alumni to manage notes, courses, requests, notices, and alumni meetups. The platform provides features such as course note sharing, suggestion and approval workflows, section swaps, thesis group finding, lost & found notices, and alumni event management.

## Features

- **User Authentication**: Secure login/logout for students, faculty, and alumni.
- **Notes Management**: Add, view, suggest edits, approve, and delete notes for courses.
- **Course Management**: Faculty can add and delete courses.
- **Section Swap**: Students can request and accept section swaps.
- **Thesis Group Finder**: Students can find or create thesis groups and manage invitations.
- **Notices**: Post, edit, and delete general and lost & found notices.
- **Alumni Meetups**: Alumni can arrange, edit, and delete meetups.
- **Request Management**: View, ignore, and manage active and ignored requests.
- **Role-Based Access**: Different permissions for students, faculty, and alumni.

## Requirements

- Python 3.10
- MySQL Server
- The following Python packages (see `requirements.txt`):

```
Flask==2.3.3
Flask-Login==0.6.3
mysql-connector-python==8.0.33
```

## Setup Instructions

1. **Clone the repository**
    ```sh
    git clone <your-repo-url>
    cd campusLink
    ```

2. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure the Database**
    - Create a MySQL database named `notesflask`.
    - Create the required tables (`user`, `student`, `courses`, `notes`, `note_suggestions`, `note_pending`, `section_swap`, `find_thesisgroup`, `accepted_invitations`, `ignored_requests`, `Notice`, `general_notice`, `lost_found_notice`, `Alumni`, etc.) according to your needs.
    - Update the database credentials in `app.py` if necessary.

4. **Run the Application**
    ```sh
    python app.py
    ```
    The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Project Structure

```
campusLink/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── home.html
│   ├── ...
│   └── alumni_meetups.html
└── README.md
```

## Usage

- **Login**: Use your user ID or email and password to log in.
- **Notes**: Browse courses and notes, suggest edits, or add new notes (faculty/students).
- **Requests**: Submit section swap or thesis group requests.
- **Notices**: Post or view general and lost & found notices.
- **Alumni**: Arrange or join meetups if you are an alumni.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is for educational purposes.

---

**Note:** Make sure to secure your secret keys and database credentials before deploying to
