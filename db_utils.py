# #  in this file: create python functions to access and update DB and use exception handling

from config import HOST, USER, PASSWORD
import mysql.connector

# exception for handling DB connection errors:


class DbConnectionError(Exception):
    pass


# connect to MySQL database (Skillshare):
def _connectDB(dbName):
    # establish DB connection using provided credentials and database name
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=dbName
    )
    return conn


""" REGISTER NEW STUDENT USER (POST)
endpoint: /register-student
functionality: allows new student users to register - creates student ID
data: student_name, student_email """


def add_student(student_name, student_email):
    try:
        # connect to DB
        dbName = 'Skillshare'
        db_connection = _connectDB(dbName)
        cur = db_connection.cursor()
        print(f'Connected to DB: {dbName}')

        # this query would only work using %s value placeholders as I was repeatedly getting an error - I referenced stack overflow for help with this: https://stackoverflow.com/questions/997797/what-does-s-mean-in-a-python-format-string
        query = """
                    INSERT INTO students (student_name, student_email)
                    VALUES (%s, %s)
                """

        # execute the query and commit to the database
        cur.execute(query, (student_name, student_email))
        db_connection.commit()

        # return the automatically generated ID that was set during the last INSERT operation:
        student_id_query = "SELECT LAST_INSERT_ID()"
        # execute SQL query
        cur.execute(student_id_query)
        # fetch the first row (and first column value) from the query result:
        student_id = cur.fetchone()[0]

        cur.close()

    except Exception:
        raise DbConnectionError(f'Failed to insert new student')
    finally:
        if db_connection:
            db_connection.close()
            print(f'{dbName} connection is closed')

    print('New student added to DB')
    return student_id


""" BOOK A CLASS (POST)
endpoint: /book-class
funtionality: student users can book a class to learn specified skills
data: student_id, skill_name """


def book_class(student_id, skill_name):
    try:
        # connect to DB
        dbName = 'Skillshare'
        db_connection = _connectDB(dbName)
        cur = db_connection.cursor()
        print(f'Connected to DB: {dbName}')

        # SQL query to insert to DB
        query = f"""
            INSERT INTO bookings (student_id, skill_name)
            VALUES (
            '{student_id}',
            '{skill_name}')
        """

        # execute the query and commit to the DB
        cur.execute(query)
        db_connection.commit()
        cur.close()
    except Exception:
        raise DbConnectionError(f'Failed to book class for student')
    finally:
        if db_connection:
            db_connection.close()
            print(f'{dbName} connection is closed')
    print('Class booked for student')


""" OFFER A SKILL (POST)
endpoint: /offer-skill
functionality: allows users to offer to teach a skill
data: skill_name, skill_description, user_name, user_availability """


def add_skill_offer(skill_name, skill_description, user_name, user_availability):
    try:
        # connect to DB
        dbName = 'Skillshare'
        db_connection = _connectDB(dbName)
        cur = db_connection.cursor()
        print(f'Connected to DB: {dbName}')

        # SQL query to insert a new skill offer into the DB
        query = f"""
            INSERT INTO skills (skill_name, skill_description, user_name, user_availability)
            VALUES (
                '{skill_name}',
                '{skill_description}',
                '{user_name}',
                '{user_availability}'
            )"""

        # execute the query and commit to the DB
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        # raise a specific exception if the insertion fails
        raise DbConnectionError(f'Failed to insert new skill offer')
    finally:
        # ensure the DB connection is closed
        if db_connection:
            db_connection.close()
            print(f'{dbName} connection is closed')

    print('New skill offer added to DB')
    return add_skill_offer


"""
# Example of adding a new skill offer:
skill_offer = {
    'skill_name': 'Cybersecurity',
    'skill_description': 'Protecting systems, networks, and programs from digital attacks',
    'user_name': 'Libby',
    'user_availability': 'Available Saturdays and Sundays'
}"""


""" SEARCH ALL SKILLS (GET)
endpoint: /skills
functionality: allows users to search for skills on offer
query parameters: skills, skill_name, skill_description, user_availability """


def _map_skill_values(skills_available):
    # map the DB records to a list of dictionaries
    mapped = []
    for skill in skills_available:
        mapped.append({
            'skill_name': skill[0],
            'skill_description': skill[1],
            'user_availability': skill[2]
        })
    return mapped


def search_skills():
    returned_skills = []
    try:
        dbName = 'Skillshare'
        # connect to DB
        db_connection = _connectDB(dbName)
        cur = db_connection.cursor()
        print(f'Connected to DB: {dbName}')

        # SQL query to retrieve all skills from the DB
        query = """
        SELECT skill_name, skill_description, user_availability
        FROM skills
        """

        cur.execute(query)

        # fetch all records and map them to a list of dictionaries
        skills_result = cur.fetchall()
        returned_skills = _map_skill_values(skills_result)
        cur.close()

    except Exception:
        # raise specific exception if the query fails
        raise DbConnectionError(f'Failed to connect to DB: {dbName}')
    finally:
        # ensure the DB connection is closed
        if db_connection:
            db_connection.close()
            print(f'{dbName} connection is closed')

    return returned_skills


"""
LEAVE REVIEW (POST)
endpoint: /leave-review
functionality: users can leave a feedback review for a skill they have learned
data: skill_name, student_id (used instead of student_name to anonymise user reviews to other users), review_rating, review_comment """


def add_new_review(skill_name, student_id, review_rating, review_comment):
    try:
        # connect to the DB
        dbName = 'Skillshare'
        db_connection = _connectDB(dbName)
        cur = db_connection.cursor()
        print(f'Connected to DB: {dbName}')

        # SQL query to insert a new review into the database
        query = f"""
                INSERT INTO review (skill_name, student_id, review_rating, review_comment)
                VALUES (
                    '{skill_name}',
                    '{student_id}',
                    '{review_rating}',
                    '{review_comment}'
                )"""

        # execute the query and commit to the DB
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        # raise a specific exception if the insertion fails
        raise DbConnectionError(f'Failed to insert new review')
    finally:
        # ensure the DB connection is closed
        if db_connection:
            db_connection.close()
            print(f'{dbName} connection is closed')

    print(f'New review added to {dbName}')
    return add_new_review


"""
# Example of adding new review: 
leave_review = {
    'skill_name': 'Data Analysis',
    'student_id': '108',
    'review_rating': 5,
    'review_comment': 'I had a great teacher to learn the skill from. Very professional and well informed.'
}"""


""" SEARCH REVIEWS (GET) by skill_name
endpoint: /reviews/<skill_name>
functionality: users can search for reviews of specific skills filtering by skill_name
query parameters: skill_name """


def _map_review_values(reviews):
    # map the DB review records to a list of dictionaries
    mapped = []
    for review in reviews:
        mapped.append({
            'skill_name': review[0],
            'student_id': review[1],
            'review_rating': review[2],
            'review_comment': review[3]
        })
    return mapped


def read_reviews(skill_name):
    returned_reviews = []

    try:
        dbName = 'Skillshare'
        # connect to the DB
        db_connection = _connectDB(dbName)
        cur = db_connection.cursor()
        print(f'Connected to DB: {dbName}')

        # SQL query to retrieve reviews for a specific skill from the DB
        query = """
                SELECT skill_name, student_id, review_rating, review_comment
                FROM review
                WHERE skill_name = '{}' """.format(skill_name)

        cur.execute(query)

        # fetch all records and map them to a list of dictionaries
        reviews_result = cur.fetchall()
        returned_reviews = _map_review_values(reviews_result)
        cur.close()

    except Exception:
        raise DbConnectionError(f'Failed to connect to {dbName}')
    finally:

        if db_connection:
            db_connection.close()
            print(f'{dbName} connection is closed')

    return returned_reviews


# main function to run programs
def main():
    pass
    # add_skill_offer()
    # print(search_skills())
    # add_new_review()
    # print(read_reviews('Web Development'))
    # add student()
    # book_class()


if __name__ == '__main__':
    main()
