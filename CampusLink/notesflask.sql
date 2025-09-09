-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 09, 2025 at 07:02 PM
-- Server version: 10.6.23-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `notesflask`
--

-- --------------------------------------------------------

--
-- Table structure for table `accepted_invitations`
--

CREATE TABLE `accepted_invitations` (
  `id` int(11) NOT NULL,
  `receiver_id` varchar(20) NOT NULL,
  `sender_id` varchar(20) NOT NULL,
  `message` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accepted_invitations`
--

INSERT INTO `accepted_invitations` (`id`, `receiver_id`, `sender_id`, `message`) VALUES
(70, 'st1', '24141104', 'Your thesis request has been accepted!\nThesis Topic: Quantum computers in Astronomy\nResearch Area: Quantum computer'),
(71, '24101664', '24141104', 'Your thesis request has been accepted!\nThesis Topic: Quantum computers in Mathematics\nResearch Area: Quantum computer'),
(72, 'st1', '24141104', 'Your thesis request has been accepted!\nThesis Topic: Sentiment Analysis on Social Media\nResearch Area: Natural Language Processing');

-- --------------------------------------------------------

--
-- Table structure for table `alumni`
--

CREATE TABLE `alumni` (
  `EvenID` int(11) NOT NULL,
  `Title` varchar(255) NOT NULL,
  `Date` date NOT NULL,
  `Location` varchar(255) NOT NULL,
  `Batch` varchar(50) NOT NULL,
  `Arranged_by` varchar(50) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alumni`
--

INSERT INTO `alumni` (`EvenID`, `Title`, `Date`, `Location`, `Batch`, `Arranged_by`, `created_at`, `updated_at`) VALUES
(4, 'CSE Batch 2018 Reunion', '2024-02-16', 'BRACU Campus, Dhaka', '2018', 'alumni1', '2025-09-06 17:53:35', '2025-09-07 02:54:37'),
(5, 'CSE Alumni Meetup', '2024-03-20', 'Gulshan, Dhaka', '2017', 'alumni2', '2025-09-06 17:53:35', '2025-09-06 17:53:35'),
(6, 'Engineering Alumni Gathering', '2024-04-10', 'Dhanmondi, Dhaka', '2019', 'alumni3', '2025-09-06 17:53:35', '2025-09-06 17:53:35');

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `courseID` char(6) NOT NULL,
  `title` varchar(30) NOT NULL,
  `description` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`courseID`, `title`, `description`) VALUES
('CSE110', 'Programming Language I', 'This course introduces foundational knowledge of string manipulation, arrays, control structure, file input/output, and the like. The debugging techniques and programming tools will make the students well-equipped in creating fundamental programs. From the anticipated outcomes of this course students will be able to: 1. Use flow control design tools, create flowcharts for solving problems. Write, debug, and execute programs using a programming language from hands-on experience. 2. Apply branching and looping structures to control program flow, and implement conditional statements, loops, and basic programming concepts to solve simple problems. Also, manipulate text data using string manipulation techniques. 3. Create, read, and modify arrays to store and process data, and sort array items using various sorting techniques.'),
('CSE111', 'Programming Language II', 'This course would be an introduction to data structures, formal specification, and syntax of Object Oriented Programming (OOP), elements of language theory, and mathematical preliminaries. Other topics that would be covered are formal languages, structured programming concepts, and a survey of the features of existing high-level languages. Students would design and write applications using an appropriate language. The course includes a compulsory 3-hour laboratory work each week.'),
('CSE220', 'Data Structure', 'This course is an introduction to data structures, where the students will study the elementary data structures such as arrays, lists, stacks, queues, trees, etc. These data structures will be used to study and implement different algorithms such as sorting, searching, tree traversal, etc. The course includes a 3 hour mandatory laboratory per week as CSE220L. In the laboratory, the students will use a standard programming language, usually Java, to implement the various data structures and algorithms learned in the theory component of the course.'),
('CSE221', 'Algorithm Analysis & Design', 'This course addresses the study of efficient algorithms, their analyses and effective algorithm design techniques. Standard algorithm design strategies, such as, Divide and Conquer paradigm, Greedy method, Dynamic programming, Backtracking, Basic search and traversal techniques, Graph algorithms, Elementary parallel algorithms, Algebraic simplification and transformations, Lower bound theory, NP-hard and NP-complete problems are discussed in the course. Examples of data structures and algorithms studied in details are Heaps; Hashing; Graph algorithms: Shortest paths, Depth-first and Breadth-first search, Network flow, Computational geometry, Minimum Spanning Tree; Integer arithmetic: GCD, primality; polynomial and matrix calculations; Sorting; Performance bounds, asymptotic analysis, worst case and average case behavior, correctness and complexity. The course includes a compulsory 3 hour laboratory work every week.'),
('CSE331', 'Automata and Computability', 'Alphabets, strings, and languages, Deterministic Finite Automata (DFA), Regular Languages, the Regular Operations, Regular Language closure properties, Nondeterminism, Nondeterministic Finite Automata (NFA), Equivalence between DFA and NFA using Subset Construction, Regular Expressions, Equivalence between Regular Expressions and Finite Automata, Converting Regular Expressions to NFA, Converting DFA into Regular Expressions using the State Elimination Method, Nonregular Languages, Pumping Lemma for Regular Languages, Context-Free Grammars (CFG) and Context-Free Languages (CFL), Parse Trees, Derivations, and Ambiguity, Chomsky Normal Form (CNF), the Cocke-Younger-Kasami (CYK) algorithm, Pushdown Automata (PDA) and its equivalence with CFGs, Turing Machines (TM), Turing-Recognizable and Turing-Decidable Languages, TM Variants, Undecidability, the Halting Problem, Reducibility.'),
('CSE370', 'Database', 'This course is designed as an introduction to relational database management systems (RDBMS) focusing on the efficient design, implementation and optimization of an RDBMS. Topics covered will include the advantages and disadvantages of DBMS, database architecture, data modeling using ER and EER models, relational integrity constraints, relational schema mapping from ER/EER, indexing, hashing and normalization. SQL Query formulation will be extensively practiced in both the theoretical and laboratory components of the course. The course includes a compulsory 3 hour laboratory work each week as CSE370L. Students must complete several hands-on SQL assignments and a group project for the laboratory work. The group project will involve the design and implementation of a complete database system including a user interface.'),
('MAT216', 'Linear Algebra and Fourier Ana', 'This course is designed to provide the learners with a solid understanding of the concepts of Linear Algebra, an indispensable part of both the fields of Computer Science and Mathematics. This is an undergraduate course for students of Engineering, Science, and Mathematics. Linear algebra is the study of linear systems of equations, vector spaces, and linear transformations. Solving systems of linear equations is a basic tool of many mathematical procedures used for solving problems in science and engineering.'),
('PHY111', 'Principles of Physics I', 'This is designed to introduce the principles of Newtonian mechanics at the freshmen level of the undergraduate study for engineering majors or equivalent. The key concepts to be developed throughout the semester are: vectors, equations of motions, Newton’s laws, conservation laws of energy, momentum, the work- energy theorem, extension of linear motion to rotational motion including the conservation laws, gravitation, elasticity and their properties, SHM.');

-- --------------------------------------------------------

--
-- Table structure for table `find_thesisgroup`
--

CREATE TABLE `find_thesisgroup` (
  `id` int(11) NOT NULL,
  `student_id` varchar(20) NOT NULL,
  `topic` varchar(100) NOT NULL,
  `research_area` varchar(50) NOT NULL,
  `group_id` varchar(20) NOT NULL,
  `members_needed` int(11) NOT NULL,
  `status` enum('pending','accepted','rejected') DEFAULT 'pending'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `find_thesisgroup`
--

INSERT INTO `find_thesisgroup` (`id`, `student_id`, `topic`, `research_area`, `group_id`, `members_needed`, `status`) VALUES
(25, 'st1', 'Quantum computers in Astronomy', 'Quantum computer', '4432', 2, 'accepted'),
(26, '24101664', 'Quantum computers in Mathematics', 'Quantum computer', '5432', 2, 'accepted'),
(27, '24141104', 'Quantum computers in Astronomy', 'Quantum computer', '6521', 2, 'pending'),
(28, '24101664', 'AI-based Traffic Management System', 'Artificial Intelligence / Computer Vision', '33211', 3, 'pending'),
(29, 'st1', 'Sentiment Analysis on Social Media', 'Natural Language Processing', '65532', 2, 'accepted');

-- --------------------------------------------------------

--
-- Table structure for table `general_notice`
--

CREATE TABLE `general_notice` (
  `notice_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `general_notice`
--

INSERT INTO `general_notice` (`notice_id`) VALUES
(1),
(3),
(5);

-- --------------------------------------------------------

--
-- Table structure for table `ignored_requests`
--

CREATE TABLE `ignored_requests` (
  `id` int(11) NOT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  `request_type` enum('thesis','section') DEFAULT NULL,
  `request_id` int(11) DEFAULT NULL,
  `ignored_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ignored_requests`
--

INSERT INTO `ignored_requests` (`id`, `user_id`, `request_type`, `request_id`, `ignored_at`) VALUES
(54, '24141104', 'section', 21, '2025-09-09 15:37:06'),
(55, '24141104', 'thesis', 28, '2025-09-09 15:37:13');

-- --------------------------------------------------------

--
-- Table structure for table `lost_found_notice`
--

CREATE TABLE `lost_found_notice` (
  `notice_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lost_found_notice`
--

INSERT INTO `lost_found_notice` (`notice_id`) VALUES
(2),
(4),
(6),
(7),
(10);

-- --------------------------------------------------------

--
-- Table structure for table `notes`
--

CREATE TABLE `notes` (
  `courseID` char(6) NOT NULL,
  `noteID` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `note` varchar(2000) DEFAULT NULL,
  `student_view` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `notes`
--

INSERT INTO `notes` (`courseID`, `noteID`, `title`, `note`, `student_view`) VALUES
('CSE221', 7, 'Introduction to Algorithms', 'Informally, an algorithm is any well-defined computational procedure that takes some value, or set of values, as input and produces some value, or set of values, as output in a finite amount of time. An algorithm is thus a sequence of computational steps that transform the input into the output. \r\nAn algorithm for a computational problem is correct if every problem instance provided as input halts or finishes its computing in finite time and outputs the correct solution to the problem instance.\r\n\r\nThere are two main criteria for judging the merits of algorithms:\r\n \r\nCorrectness (does the algorithm solve the problem in a finite number of steps?) \r\nEfficiency (how much resources in terms of memory and time does it take to execute?)\r\n\r\nDefinition: A finite set of statements that guarantees an optimal solution in a finite interval of time.\r\n', 1),
('CSE370', 23, 'The Mini World', 'The mini world concept is essential in ER modeling. It helps in\r\nidentifying and defining the relevant entities and relationships\r\nrequired for database design.\r\n\r\nMini world is some part of the real world about which data is\r\nstored in a database. For example, if we want to create a\r\ndatabase for train reservation in Bangladesh, then the train\r\nreservation system is the mini-world. Similarly, if we want to\r\ncreate a database for a university, then that University is the\r\nmini-world that we will represent in our database.\r\n\r\nNote, the mini-world is not shown on the ER diagram.', 1),
('CSE370', 24, 'Entities and Entity Types', 'Entities are specific objects or things in the mini-world that are\r\nrepresented in the database.\r\n\r\nFor example, the STUDENT Sakib Chowdhury, the CSE\r\nDEPARTMENT or the course CSE370 are all entities in the\r\nUniversity mini-world. Thus, if there are 5000 students enrolled in\r\nthe university, then they are all 5000 individual entities.\r\n\r\nAll these 5000 students have similar type of information stored\r\nabout them and they have the same role within the mini-world, so\r\nthey can be grouped together into the Student entity type. So,\r\nwhen several entities are grouped together due to sharing the\r\nsame properties and role then it is called the Entity Type.\r\n\r\nEntity types are shown in ER diagram using a \"rectangle\" shape.', 1),
('CSE370', 25, 'Attributes (1)', 'Attributes are properties used to describe an entity. For example,\r\na STUDENT may have attributes such as id, name, cgpa, email,\r\netc. A specific entity will have a value for each of its attributes.\r\nThere are 3 types of Attributes:\r\n\r\nSimple: Each entity has a single atomic value for the attribute.\r\nFor example, STUDENT id, cgpa, EMPLOYEE salary. It is shown\r\nusing an \"oval\" shape in the ER diagram.\r\n\r\nMultivalued: An entity may have multiple values for that attribute.\r\nFor example, color of a CAR or email of a STUDENT. It is shown\r\nusing a \"double oval\" shape in the ER.\r\n\r\nComposite: Each value of the attribute is composed of several\r\ncomponents. For example, Address(Apt#, House#, Street, City,\r\nState, ZipCode, Country), or Name(FirstName MiddleName\r\nLastName). Some components may themselves be composite.\r\n\"Ovals\" are connected to other \"ovals\" in the ER.\r\n\r\nAn attribute can be composite-multivalued, for example, previous\r\ndegrees of a STUDENT.', 1),
('CSE370', 26, 'Attributes (2)', 'Key Attribute\r\nAn attribute of an entity type for which each entity must have a\r\nunique value is called a key attribute of the entity type. For\r\nexample, Student ID or email, Course code.\r\n\r\nKey attributes are \"underlined\" in the ER diagram. An entity\r\ncan have more than one key attribute. A key attribute should not\r\nbe multivalued.\r\n\r\nDerived Attribute\r\nAn attribute value that can be calculated/derived from other\r\nstored data, it is called a derived attribute. It means the value will\r\nnot be stored in the database, but instead will be derived when\r\nneeded in order to save space.\r\n\r\nFor example, \"total bill\" of an ORDER when the unit price and\r\nquantity is stored, \"age\" of a STUDENT when birthdate is stored.\r\nDerived attribute is shown using a \"dotted oval\" in ER diagram.', 0),
('CSE370', 27, 'Weak Entity', 'Sometimes an entity may not have any unique (key) attributes.\r\nIn such cases the individual entities cannot be uniquely\r\nidentified using its own attributes. Such entities belong to weak\r\nentity types. The example of SECTIONS in a university mini-\r\nworld (on the left) illustrates a weak entity type.\r\n\r\nWeak entity types are shown using a \"double rectangle\" in the\r\nER diagram and such an entity type must not have any key\r\nattributes.\r\n\r\nPartial Key\r\nA weak entity may not have a key attribute, but it may have an\r\nattribute that is \"part\" of a unique key/value. Such an attribute is\r\ncalled a partial key and is shown using a \"dotted underline\".\r\nOn the left Section Number is not unique as many sections (of\r\ndifferent courses) will have the same number. But the section\r\nnumber is part of the key that will be used to identify a particular\r\nsection.', 1),
('CSE370', 28, 'Relationships', 'A relationship relates two or more distinct entities with a\r\nspecific meaning. For example, EMPLOYEE John Smith works\r\non the ProductX PROJECT, or STUDENT Ahnaf Atef enrolls in\r\nthe CSE370 COURSE. Relationships of the same type are\r\ngrouped together into a relationship type.\r\n\r\nRelationship types are shown using a \"diamond\" shape\r\nconnected to the related entity types.\r\n\r\nRelationship types may or may not have attributes. In the\r\nexample, \"grade\" is a relationship attribute because unless a\r\nSTUDENT enrolls in a particular COURSE, there will be no grade for\r\nthat student. Thus, the grade value will only exist if a relationship is\r\nestablished between a specific student and a specific course.\r\n\r\nThe same entity types may have different relationships between\r\nthem, each relationship type conveying different meanings. For\r\nexample, STUDENT and COURSE have two different relationship\r\ntypes: \"enrolls_in\" and \"ST_of\".', 1);

-- --------------------------------------------------------

--
-- Table structure for table `note_pending`
--

CREATE TABLE `note_pending` (
  `ID` int(11) NOT NULL,
  `courseID` varchar(6) NOT NULL,
  `title` varchar(200) NOT NULL,
  `note` varchar(2000) NOT NULL,
  `post_by` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `note_pending`
--

INSERT INTO `note_pending` (`ID`, `courseID`, `title`, `note`, `post_by`) VALUES
(8, 'CSE331', 'wqerfgh', 'wfegrhtyhujk', 'st1'),
(25, 'CSE370', 'Relationship Constraints (1)', 'Cardinality Ratio (specifies maximum participation):\r\n\r\nShown in the ER by placing appropriate numbers on the\r\nrelationship edges:\r\n\r\nOne-to-one (1:1): A single entity in one entity type is\r\nrelated to a single entity in the other entity type. E.g. 1\r\nFACULTY member can coordinate only 1 COURSE at a\r\ntime and a COURSE will have only 1 COORDINATOR.\r\n\r\nOne-to-many (1:N) or Many-to-one (N:1): An entity\r\nfrom one type can be related to multiple entities from\r\nthe other entity type, or vice versa. 1 COURSE has many\r\nSECTIONs, but a SECTION belongs to only 1 COURSE.\r\n\r\nMany-to-many (M:N): Multiple entities from one type\r\nare related to multiple entities from the other type. Many\r\nSTUDENTS are enrolled in a SECTION, and a SECTION\r\nhas many STUDENTS in it.\r\nrelationship.\r\n\r\nA relationship of degree n is called an n-ary\r\nrelatiosnhip, meaning \"n\" number of entity types are\r\nparticipating in that relationship.', '24141104'),
(26, 'CSE221', 'fdghjkl;', 'vgfytugvhguyijk', '24141104');

-- --------------------------------------------------------

--
-- Table structure for table `note_suggestions`
--

CREATE TABLE `note_suggestions` (
  `courseID` char(6) NOT NULL,
  `noteID` int(11) NOT NULL,
  `suggestionID` int(11) NOT NULL,
  `suggestion` varchar(2000) NOT NULL,
  `suggested_by` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `note_suggestions`
--

INSERT INTO `note_suggestions` (`courseID`, `noteID`, `suggestionID`, `suggestion`, `suggested_by`) VALUES
('CSE370', 23, 35, 'efgrhtyghj,yjtrhtjThe mini world concept is essential in ER modeling. It helps in\r\nidentifying and defining the relevant entities and relationships\r\nrequired for database design.\r\n\r\nMini world is some part of the real world about which data is\r\nstored in a database. For example, ifewtyrtul', '24141104'),
('CSE370', 27, 36, 'Sometimes an entity may not have any unique (key) attributes.\r\nIn such cases the individual entities cannot be uniquely\r\nidentified using its own attributes. Such entities belong to weak\r\nentity types. The example of SECTIONS in a university mini-\r\nworld (on the left) illustrates a weak entity type.\r\n\r\nWeak entity types are shown using a \"double rectangle\" in the\r\nER diagram and such an entity type must not have any key\r\nattributes (but may have partial key attribute).\r\n\r\nPartial Key\r\nA weak entity may not have a key attribute, but it may have an\r\nattribute that is \"part\" of a unique key/value. Such an attribute is\r\ncalled a partial key and is shown using a \"dotted underline\".\r\nOn the left Section Number is not unique as many sections (of\r\ndifferent courses) will have the same number. But the section\r\nnumber is part of the key that will be used to identify a particular\r\nsection.', '24141104'),
('CSE221', 7, 41, 'Informally, an algorithm is any well-defined computational procedure that takes some value, or set of values, as input and produces some value, or set of values, as output in a finite amount of time. An algorithm is thus a sequence of computational steps that transform the input into the output. \r\nAn algorithm for a computational problem is correct if every problem instance provided as input halts or finishes its computing in finite time and outputs the correct solution to the problem instance.\r\n\r\nThere are two main criteria for judging the merits of algorithms:\r\n \r\nCorrectness (does the algorithm solve the problem in a finite number of steps?) \r\nEfficiency (how much resources in terms of memory and time does it take to execute?)\r\n\r\nDefinition: A finite set of statements that guarantees an optimal solution in a finite interval of time.\r\n\r\nNew suggestion\r\n', '24141104');

-- --------------------------------------------------------

--
-- Table structure for table `notice`
--

CREATE TABLE `notice` (
  `notice_id` int(11) NOT NULL,
  `description` text DEFAULT NULL,
  `title` varchar(200) NOT NULL,
  `type` varchar(20) NOT NULL,
  `posted_by` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `notice`
--

INSERT INTO `notice` (`notice_id`, `description`, `title`, `type`, `posted_by`) VALUES
(1, 'Welcome to our new notice board system!', 'Welcome to CampusLink', 'general', 'teacher1'),
(2, 'Found a phone in Room 101. Contact if it is yours.', 'Lost Phone Found', 'lost_found', 'student1'),
(3, 'Faculty meeting tomorrow at 2 PM in Conference Room.', 'Important Meeting', 'general', 'teacher1'),
(4, 'Lost my keys near the library. Please help find them.', 'Lost Keys', 'lost_found', 'student1'),
(5, 'University will be closed on Friday for holiday.', 'Holiday Notice', 'general', 'teacher1'),
(6, 'test, lost my dog', 'Notice title', 'lost_found', 'teacher1'),
(7, 'Lost my CSE370 notebook at 12F-32L. Please leave it as lost and found counter.', 'Lost My 370 notebook', 'lost_found', '24141104'),
(10, 'I lost my phone around 2 pm in the campus.', 'Lost my phone ', 'lost_found', '24141104');

-- --------------------------------------------------------

--
-- Table structure for table `section_swap`
--

CREATE TABLE `section_swap` (
  `id` int(11) NOT NULL,
  `student_id` varchar(20) NOT NULL,
  `course_code` varchar(10) NOT NULL,
  `current_section` varchar(10) NOT NULL,
  `desired_section` varchar(10) NOT NULL,
  `status` enum('pending','accepted','rejected') DEFAULT 'pending'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `section_swap`
--

INSERT INTO `section_swap` (`id`, `student_id`, `course_code`, `current_section`, `desired_section`, `status`) VALUES
(15, '24141104', 'CSE331', '10', '18', 'accepted'),
(16, '24141104', 'CSE221', '4', '17', 'accepted'),
(17, 'st1', 'MAT215', '20', '4', 'accepted'),
(18, 'st1', 'MAT215', '20', '4', 'accepted'),
(19, '24141104', 'CSE331', '3', '3', 'accepted'),
(20, 'st1', 'CSE370', '20', '1', 'pending'),
(21, '24101664', 'MAT215', '19', '6', 'pending'),
(22, '24141104', 'CSE331', '10', '18', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL,
  `user_ID` varchar(50) NOT NULL,
  `cgpa` decimal(3,2) DEFAULT 0.00,
  `department` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`student_id`, `user_ID`, `cgpa`, `department`) VALUES
(1, '24101664', 3.75, 'CSE'),
(2, '24141104', 3.90, 'CS'),
(3, 'st1', 3.80, 'CSE');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_ID` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(22) NOT NULL,
  `name` varchar(25) NOT NULL,
  `department` varchar(3) NOT NULL,
  `user_type` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_ID`, `email`, `password`, `name`, `department`, `user_type`) VALUES
('24101664', 'ramisa@bracu.com', 'passwords', 'Ramisa Ridhi', 'CSE', 'student'),
('24101667', 'arannita@bracu.com', 'passwords', 'arannita', 'CSE', 'student'),
('24141104', 'rayan@bracu.bd', 'passwords', 'Rayan', 'CS', 'student'),
('alumni1', 'alumni1@email.com', 'passwords', 'MR. alumni1', 'CSE', 'alumni'),
('alumni2', 'alumni2@gmail.com', 'passwords', 'MR. alumni2', 'MNS', 'alumni'),
('alumni3', 'alu@email.com', 'passwords', 'Alumni3 name', 'PHY', 'alumni'),
('st1', 'st@email.com', 'passwords', 'Mr. St', 'CSE', 'st'),
('student1', 'student1@email.com', 'passwords', 'Siam', 'MNS', 'student'),
('teacher1', 'teacher@email.com', 'passwords', 'Mr. Teacher', 'CSE', 'faculty');

-- --------------------------------------------------------

--
-- Table structure for table `user_thesis_action`
--

CREATE TABLE `user_thesis_action` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `thesis_request_id` int(11) NOT NULL,
  `action` enum('accepted','rejected') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accepted_invitations`
--
ALTER TABLE `accepted_invitations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `receiver_id` (`receiver_id`),
  ADD KEY `sender_id` (`sender_id`);

--
-- Indexes for table `alumni`
--
ALTER TABLE `alumni`
  ADD PRIMARY KEY (`EvenID`),
  ADD KEY `idx_alumni_date` (`Date`),
  ADD KEY `idx_alumni_batch` (`Batch`),
  ADD KEY `idx_alumni_arranged_by` (`Arranged_by`);

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`courseID`);

--
-- Indexes for table `find_thesisgroup`
--
ALTER TABLE `find_thesisgroup`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `group_id` (`group_id`),
  ADD UNIQUE KEY `group_id_2` (`group_id`),
  ADD KEY `student_id` (`student_id`);

--
-- Indexes for table `general_notice`
--
ALTER TABLE `general_notice`
  ADD PRIMARY KEY (`notice_id`);

--
-- Indexes for table `ignored_requests`
--
ALTER TABLE `ignored_requests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `lost_found_notice`
--
ALTER TABLE `lost_found_notice`
  ADD PRIMARY KEY (`notice_id`);

--
-- Indexes for table `notes`
--
ALTER TABLE `notes`
  ADD PRIMARY KEY (`noteID`),
  ADD KEY `courseID` (`courseID`);

--
-- Indexes for table `note_pending`
--
ALTER TABLE `note_pending`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `fk_course` (`courseID`),
  ADD KEY `fk_user` (`post_by`);

--
-- Indexes for table `note_suggestions`
--
ALTER TABLE `note_suggestions`
  ADD PRIMARY KEY (`suggestionID`),
  ADD KEY `fk_suggested_by` (`suggested_by`),
  ADD KEY `fk_lectureID` (`noteID`);

--
-- Indexes for table `notice`
--
ALTER TABLE `notice`
  ADD PRIMARY KEY (`notice_id`),
  ADD KEY `posted_by` (`posted_by`);

--
-- Indexes for table `section_swap`
--
ALTER TABLE `section_swap`
  ADD PRIMARY KEY (`id`),
  ADD KEY `student_id` (`student_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`),
  ADD KEY `user_ID` (`user_ID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_ID`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `user_thesis_action`
--
ALTER TABLE `user_thesis_action`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`,`thesis_request_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accepted_invitations`
--
ALTER TABLE `accepted_invitations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `alumni`
--
ALTER TABLE `alumni`
  MODIFY `EvenID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `find_thesisgroup`
--
ALTER TABLE `find_thesisgroup`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `ignored_requests`
--
ALTER TABLE `ignored_requests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `notes`
--
ALTER TABLE `notes`
  MODIFY `noteID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `note_pending`
--
ALTER TABLE `note_pending`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `note_suggestions`
--
ALTER TABLE `note_suggestions`
  MODIFY `suggestionID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `notice`
--
ALTER TABLE `notice`
  MODIFY `notice_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `section_swap`
--
ALTER TABLE `section_swap`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user_thesis_action`
--
ALTER TABLE `user_thesis_action`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accepted_invitations`
--
ALTER TABLE `accepted_invitations`
  ADD CONSTRAINT `accepted_invitations_ibfk_1` FOREIGN KEY (`receiver_id`) REFERENCES `user` (`user_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `accepted_invitations_ibfk_2` FOREIGN KEY (`sender_id`) REFERENCES `user` (`user_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `alumni`
--
ALTER TABLE `alumni`
  ADD CONSTRAINT `alumni_ibfk_1` FOREIGN KEY (`Arranged_by`) REFERENCES `user` (`user_ID`) ON DELETE CASCADE;

--
-- Constraints for table `find_thesisgroup`
--
ALTER TABLE `find_thesisgroup`
  ADD CONSTRAINT `find_thesisgroup_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `user` (`user_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `general_notice`
--
ALTER TABLE `general_notice`
  ADD CONSTRAINT `general_notice_ibfk_2` FOREIGN KEY (`notice_id`) REFERENCES `notice` (`notice_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ignored_requests`
--
ALTER TABLE `ignored_requests`
  ADD CONSTRAINT `ignored_requests_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_ID`);

--
-- Constraints for table `lost_found_notice`
--
ALTER TABLE `lost_found_notice`
  ADD CONSTRAINT `lost_found_notice_ibfk_1` FOREIGN KEY (`notice_id`) REFERENCES `notice` (`notice_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `notes`
--
ALTER TABLE `notes`
  ADD CONSTRAINT `fk_notes_course` FOREIGN KEY (`courseID`) REFERENCES `courses` (`courseID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `note_pending`
--
ALTER TABLE `note_pending`
  ADD CONSTRAINT `fk_course` FOREIGN KEY (`courseID`) REFERENCES `courses` (`courseID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_user` FOREIGN KEY (`post_by`) REFERENCES `user` (`user_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `note_suggestions`
--
ALTER TABLE `note_suggestions`
  ADD CONSTRAINT `fk_lectureID` FOREIGN KEY (`noteID`) REFERENCES `notes` (`noteID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_suggested_by` FOREIGN KEY (`suggested_by`) REFERENCES `user` (`user_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `notice`
--
ALTER TABLE `notice`
  ADD CONSTRAINT `notice_ibfk_1` FOREIGN KEY (`posted_by`) REFERENCES `user` (`user_ID`);

--
-- Constraints for table `section_swap`
--
ALTER TABLE `section_swap`
  ADD CONSTRAINT `section_swap_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `user` (`user_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`user_ID`) REFERENCES `user` (`user_ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
