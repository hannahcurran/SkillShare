CREATE DATABASE Skillshare;
USE Skillshare;

-- create the skills table
CREATE TABLE skills (
    skill_id INT AUTO_INCREMENT UNIQUE,
    skill_name VARCHAR(255) PRIMARY KEY,
    skill_description TEXT,
    user_name VARCHAR(55),
    user_availability VARCHAR(255)
);

-- create the students table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL,
    student_email VARCHAR(255) UNIQUE NOT NULL
);

-- create the bookings table
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    skill_name VARCHAR(255),
    booking_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (skill_name) REFERENCES skills(skill_name)
);

-- create the review table 
CREATE TABLE review (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    skill_name VARCHAR(255),
    student_id INT,
    review_rating INT, -- rating score out of 5
    review_comment TEXT,
    FOREIGN KEY (skill_name) REFERENCES skills(skill_name),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

    
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

-- SELECT * FROM review;
-- SELECT * FROM skills;
-- SELECT * FROM students;
-- SELECT * FROM bookings;