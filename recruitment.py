# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
def get_skills():
    """returns a list of assigned skills"""
    return ["Cooking", "Baking", "Grilling", "Roasting"]


# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything #loop over each one and print it(Its all printing)
def show_skills(skills):
    """prints skills_list numbered to user"""
    print ("Skills: ")
    for index, skill in enumerate(skills, 1):
        print(f"{index}. {skill}")


# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    """Return a list of the two skills that the user inputted"""
    # new_user_list = []
    # skillsC = get_skills()
    # chosen_number_1 = int(input ("Choose a skill from above by entering its number: "))
    # chosen_number_2 = int(input ("Choose another skill from above by entering its number: "))
    # new_user_list.append(skillsC[chosen_number_1 -1])
    # new_user_list.append(skillsC[chosen_number_2 -1])
    # return new_user_list
    show_skills(skills)
    skill_1 = int(input("Enter the number of a skill you know: "))
    skill_2 = int(input("Enter the number of another skill you know: "))
    user_skills = [skills[skill_1 -1], skills[skill_2 -1]]
    return user_skills


    # chosen_number_1 = input ("Choose a skill from above by entering its number: ")
    # if chosen_number_1 == "1":
    #     new_user_list.append ("cooking")
    # elif chosen_number_1 == "2":
    #     new_user_list.append ("baking")
    # elif chosen_number_1 == "3":
    #     new_user_list.append ("grilling")
    # elif chosen_number_1 == "4":
    #     new_user_list.append ("roasting")
    # else:
    #     print ("Flase entry")
    # chosen_number_2 = input ("Choose another skill from above by entering its number: ")
    # if chosen_number_2 == "1":
    #     new_user_list.append ("cooking")
    # elif chosen_number_2 == "2":
    #     new_user_list.append ("baking")
    # elif chosen_number_2 == "3":
    #     new_user_list.append ("grilling")
    # elif chosen_number_2 == "4":
    #     new_user_list.append ("roasting")
    # else:
    #     print ("Flase entry")
    # return new_user_list

# x = get_skills
# y = show_skills (x)
# z = get_user_skills (y)
# print (z)

# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    """get the user's cv from their inputs"""
    cv = {}
    cv ["name"] = input ("What's your name? ")
    cv ["age"] = int(input ("How old are you? "))
    cv ["experience"] = int(input ("How many years of experience do you have? "))
    cv ["skills"] = get_user_skills(skills)
    return cv


# This functions checks if the cv is acceptable or not, by checking the age,
# experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if 25 <= cv ["age"] <= 40 and cv ["experience"] > 3 and desired_skill in cv ["skills"]:
        return True
    else:
        return False

def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the special recruitment program, please answer the following questions: ")
    skills = get_skills()
    user_cv = get_user_cv(skills)
    is_accepted = check_acceptance(user_cv, "Roasting")
    if is_accepted:
        print(f"You've been accepted, {user_cv['name']}!")
    else:
        print("Sorry, you've been rejected!")
    


if __name__ == "__main__":
    main()
