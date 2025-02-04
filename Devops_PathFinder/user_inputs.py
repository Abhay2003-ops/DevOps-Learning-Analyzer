# file to get user inputs for the progress
import constants  

def get_basic_user_info():
    
    user_name = input(constants.USER_NAME_PROMPT)
    user_education = input(constants.USER_EDUCATION_PROMPT)
    
    while True:
        user_expertise = input(constants.USER_EXPERTISE_PROMPT).capitalize()
        if user_expertise in constants.VALID_EXPERTISE_LEVELS:
            break
        print(" Invalid input! Please enter 'Beginner', 'Intermediate', or 'Expert'.")

    user_data = {
        "name": user_name,
        "education": user_education,
        "expertise": user_expertise
    }
    
    return user_data
