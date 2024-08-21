# create API endpoints in this file

from flask import Flask, jsonify, request
from db_utils import add_skill_offer, search_skills, add_new_review, read_reviews, add_student, book_class

# setup Flask app
app = Flask(__name__)


""" REGISTER NEW STUDENT 
endpoint: /register-student"""


@app.route('/register-student', methods=['POST'])
def register_student():
    # get JSON data from the request
    data = request.json

    student_name = data.get('student_name')
    student_email = data.get('student_email')

    # add the new student registration to the DB using the data provided in the request
    student_id = add_student(
        student_name=student_name,
        student_email=student_email
    )

    # return the response with student_id included
    data['student_id'] = student_id
    new_student = data
    return jsonify(new_student)


""" BOOK A CLASS 
endpoint: /book-class"""


@app.route('/book-class', methods=['POST'])
def book_class_endpoint():
    booking_details = request.get_json()
    book_class(
        student_id=booking_details['student_id'],
        skill_name=booking_details['skill_name']
    )
    return booking_details


""" OFFER A SKILL (POST)
endpoint: /offer-skill """


@app.route('/offer-skill', methods=['POST'])
def post_skill():
    # get JSON data from the request
    offer_new_skill = request.get_json()

    # add the new skill offer to the DB using the data provided in the request
    add_skill_offer(
        skill_name=offer_new_skill['skill_name'],
        skill_description=offer_new_skill['skill_description'],
        user_name=offer_new_skill['user_name'],
        user_availability=offer_new_skill['user_availability']
    )

    # return the data that was received as the response
    return offer_new_skill


""" SEARCH ALL SKILLS (GET)
endpoint: /skills """


@app.route('/skills', methods=['GET'])
def get_skills():
    # retrieve all skill offers from the DB
    results = search_skills()

    # return the skill offers as a JSON response
    return jsonify(results)


"""
LEAVE REVIEW (POST)
endpoint: /leave-review """


@app.route('/leave-review', methods=['POST'])
def post_review():
    # get JSON data from the request
    add_review = request.get_json()

    # add the new review to the database using the data provided in the request
    add_new_review(
        skill_name=add_review['skill_name'],
        student_id=add_review['student_id'],
        review_rating=add_review['review_rating'],
        review_comment=add_review['review_comment']
    )

    # return the data that was received as the response
    return add_review


""" SEARCH REVIEWS (GET) by skill_name
endpoint: /reviews """


@app.route('/reviews/<skill_name>', methods=['GET'])
def get_reviews(skill_name):
    # retrieve all reviews for a specific skill from the DB
    results = read_reviews(skill_name)

    # return the reviews as a JSON response
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
