# in this file: create client side for the API endpoints created
# only runs when app.py is running

import requests
import json


# function to register a new student
def register_student(student_name, student_email):
    new_student = {
        "student_name": student_name,
        "student_email": student_email
    }
    result = requests.post(
        'http://127.0.0.1:5000/register-student',
        headers={'content-type': 'application/json'},
        data=json.dumps(new_student)
    )

    return result.json()


# function to book a class
def book_class(student_id, skill_name):
    booking_details = {
        "student_id": student_id,
        "skill_name": skill_name
    }
    result = requests.post(
        'http://127.0.0.1:5000/book-class',
        headers={'content-type': 'application/json'},
        data=json.dumps(booking_details)
    )
    return result.json()


# function to post a new skill offer to the api
def post_skill(skill_name, skill_description, user_name, user_availability):

    # create a dictionary with the skill offer data
    skill_offer = {
        "skill_name": skill_name,
        "skill_description": skill_description,
        "user_name": user_name,
        "user_availability": user_availability
    }

    # make a post request to the api endpoint with the skill offer data
    result = requests.post(
        'http://127.0.0.1:5000/offer-skill',
        headers={'content-type': 'application/json'},
        data=json.dumps(skill_offer)
    )

    # return the response in json format
    return result.json()


# function to get all skill offers from the api
def search_skills():
    # make a get request to the api endpoint
    result = requests.get(
        'http://127.0.0.1:5000/skills',
        headers={'content-type': 'application/json'}
    )

    # return the response in json format
    return result.json()


# function to post a new review to the api
def post_review(skill_name, student_id, review_rating, review_comment):

    # create a dictionary with the review data
    new_review = {
        "skill_name": skill_name,
        "student_id": student_id,
        "review_rating": review_rating,
        "review_comment": review_comment
    }

    # make a post request to the api endpoint with the review data
    result = requests.post(
        'http://127.0.0.1:5000/leave-review',
        headers={'content-type': 'application/json'},
        data=json.dumps(new_review)
    )

    # return the response in json format
    return result.json()


# function to get all reviews for a specific skill from the api
def search_reviews(skill_name):
    # make a get request to the api endpoint with the skill name
    result = requests.get(
        'http://127.0.0.1:5000/reviews/{}'.format(skill_name),
        headers={'content-type': 'application/json'}
    )

    # return the response in json format
    return result.json()


# main function to run the client side program
def run():
    print()
    print('Hello, welcome to Skillshare - where you can offer to teach a skill or search for a new skill to be taught!')
    print()
    print('########## REGISTER/ LOGIN ############')
    print()

    # prompt user to register as a new student
    register = input(
        'Are you a new student? Would you like to register? (Y/N): ').upper()
    if register == 'Y':
        student_name = input('Enter your name: ')
        student_email = input('Enter your email: ')
        student = register_student(student_name, student_email)
        print('Thank you for registering!')
        print(f'Your student ID is: {student["student_id"]}')
        student_id = student["student_id"]
    else:
        student_id = int(input('Enter your student ID: '))

    print()
    print('########## SKILLS ############')
    print()

    # prompt user to see available skills
    skill = input(
        'Would you like to take a look at the available skills on offer to learn? (Y/N): ').upper()
    print()

    # display skills results if user wants to see them
    if skill == 'Y':
        print(search_skills())
    print()
    print('##################')
    print()

    # prompt user to offer a new skill
    new_skill = input(
        'Do you have any skills you would like to offer to teach? (Y/N): ').upper()
    print()

    # if user wants to add a new skill, collect details and post to API
    add = new_skill == 'Y'
    if add:
        skill_name = input('Enter the skill name: ')
        skill_description = input(
            'Enter a brief description of what the skill is and what you will teach: ')
        user_name = input('Enter your name: ')
        user_availability = input('Enter your availability each week: ')
        post_skill(skill_name, skill_description, user_name, user_availability)
        print()
        print('Thank you - your skill offer has been added successfully!')
        print()

    print('########## BOOK A CLASS ############')
    print()

    # prompt user to book a class
    book = input('Would you like to book a class? (Y/N): ').upper()
    if book == 'Y':
        skill_name = input(
            'Enter the skill name for the class you would like to book (eg Web Development, Yoga, Photography, Knitting, Cooking, Data Analysis): ')
        book_class(student_id, skill_name)
        print('Thank you - your class has been booked successfully!')
    print()
    print()

    # prompt user to see reviews
    print('########## REVIEWS ############')
    print()

    reviews = input(
        "Would you like to read any available reviews that students have left about the skills they've learned? (Y/N): ").upper()
    print()

    # if user wants to see reviews then fetch and display them
    if reviews == 'Y':
        skill_name = input(
            "Enter the skill name to view any available reviews (eg Graphic Design, Data Analysis, Web Development, Tennis, Knitting, Juggling): ")
        print()
        reviews = search_reviews(skill_name)
        print(json.dumps(reviews))
        print()

    print('##################')
    print()

    # prompt user to leave a review
    leave_a_review = input(
        'Would you like to leave a review if you have taken any of our skill lessons before? (Y/N): ').upper()
    print()
    add_new_review = leave_a_review == 'Y'

    # if user wants to leave a review, collect details and post to API
    if add_new_review:
        print()
        skill_name = input('Enter the name of the skill lesson you took: ')
        student_id = input('Enter your ID: ')
        review_rating = input(
            'Enter a review score (0 (poor) - 5 (excellent)): ')
        review_comment = input('Enter your review comment: ')
        post_review(skill_name, student_id, review_rating, review_comment)
        print()
        print('Thank you - your review has been added successfully!')
        print()

    print('##################')
    print()
    print('Thank you for visiting Skillshare. We look forward to seeing you again soon!')
    print()


if __name__ == '__main__':
    run()
