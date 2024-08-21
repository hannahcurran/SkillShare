### SkillShare API:
A platform where users can offer to teach a skill and others can search available skills to learn. Student users can register and are able to book skills lessons. Student users can also leave review feedback for the lessons they have attended and read reviews other users have posted.


### Setup
# 1. Database Setup:
1.1 Set up the MySQL database called `Skillshare`.
1.2 Create the following tables:
        `skills`: to store skill lesson offers.
        `students`: to store student user information which is used to register to book classes.
        `bookings`: to store bookings for skill lessons.
        `review`: to store reviews left by users.

1.3 Insert dummy data into the tables: 

-- insert dummy data into students table
INSERT INTO students (student_id, student_name, student_email) VALUES
(101, 'Alice', 'alice@example.com'),
(102, 'Bob', 'bob@example.com'),
(103, 'Charlie', 'charlie@example.com'),
(104, 'David', 'david@example.com'),
(105, 'Eve', 'eve@example.com'),
(106, 'Frank', 'frank@example.com'),
(107, 'Grace', 'grace@example.com'),
(108, 'Hank', 'hank@example.com'),
(109, 'Ivy', 'ivy@example.com'),
(110, 'Jack', 'jack@example.com');

-- insert dummy data into skills table
INSERT INTO skills (skill_id, skill_name, skill_description, user_name, user_availability) VALUES
(1, 'Graphic Design', 'Learn the fundamentals of graphic design using modern tools and techniques.', 'Libby', 'Available Mondays and Wednesdays'),
(2, 'Data Analysis', 'Understand and apply data analysis techniques to real-world datasets.', 'Alex', 'Available Tuesdays and Thursdays'),
(3, 'Web Development', 'Build and deploy web applications using HTML, CSS, and JavaScript.', 'Jordan', 'Available Fridays and Saturdays'),
(4, 'Tennis', 'Improve your tennis skills with professional coaching.', 'Morgan', 'Available Sundays'),
(5, 'Knitting', 'Master the art of knitting from beginner to advanced levels.', 'Taylor', 'Available Wednesdays and Fridays'),
(6, 'Photography', 'Capture stunning photos with our comprehensive photography course.', 'Casey', 'Available Mondays and Saturdays'),
(7, 'Cooking', 'Learn to cook delicious meals with our step-by-step classes.', 'Jamie', 'Available Tuesdays and Thursdays'),
(8, 'Yoga', 'Enhance your well-being with our guided yoga sessions.', 'Riley', 'Available Mondays and Fridays'),
(9, 'Spanish', 'Learn to speak Spanish fluently with immersive lessons.', 'Avery', 'Available Wednesdays and Sundays'),
(10, 'Music Theory', 'Understand the principles of music theory and composition.', 'Peyton', 'Available Thursdays and Saturdays');


-- insert dummy data into review table
INSERT INTO review (review_id, skill_name, student_id, review_rating, review_comment) VALUES
(1, 'Graphic Design', 101, 5, 'Amazing course! I learned a lot about design principles and tools.'),
(2, 'Data Analysis', 102, 4, 'Very informative, but could use more real-world examples.'),
(3, 'Web Development', 103, 5, 'Great instructor and comprehensive coverage of topics.'),
(4, 'Tennis', 104, 3, 'Good for beginners, but not challenging enough for intermediate players.'),
(5, 'Knitting', 105, 4, 'Well-structured and easy to follow.'),
(6, 'Photography', 106, 5, 'Loved the practical tips and hands-on approach.'),
(7, 'Cooking', 107, 4, 'Learned some great new recipes, but could use more detailed instructions.'),
(8, 'Yoga', 108, 5, 'Excellent class with clear instructions and great pacing.'),
(9, 'Spanish', 109, 4, 'Effective teaching methods, but the pace was a bit fast for me.'),
(10, 'Music Theory', 110, 5, 'In-depth and very well explained. Highly recommend.');

# 2. Configuration: 
edit the `config.py` file to include your MySQL database credentials (HOST, USER, PASSWORD).

# 3. Installation Requirements:
3.1 Ensure Python3 is installed.
3.2 Install required Python packages using pip: `pip install flask mysql-connector-python`

# 4. Running the API:
4.1 Start the Flask application by running app.py: `python app.py`.
4.2 Ensure `main.py` is also running concurrently to interact with the API: `python main.py`.


### API Endpoints
# 1. Offer a Skill (POST)
endpoint: /offer-skill
functionality: allows users to offer to teach a skill.
data: skill_name, skill_description, user_name, user_availability.

# 2. Search All Skills (GET)
endpoint: /skills
functionality: allows users to search for skills on offer.

# 3. Leave Review (POST)
endpoint: /leave-review
functionality: Users can leave a feedback review for a skill they have learned. Reviews use student_id instead of student_name to provide more anonymity amongst users. 
data: skill_name, student_id, review_rating, review_comment.

# 4. Search Reviews (GET) by skill_name
endpoint: /reviews/<skill_name>
functionality: users can search for reviews of specific skills by skill_name.

# 5. Register New Student User (POST)
endpoint: /register-student
functionality: allows new student users to register to SkillShare- creates student ID
data: student_name, student_email

# 6. Book a Class (POST) 
endpoint: /book-class
funtionality: student users can book a class to learn specified skills
data: student_id, skill_name
