# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
def get_skills():
    """returns a list of assigned skills"""
    return ["cooking", "baking", "grilling", "roasting"]


# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything #loop over each one and print it(Its all printing)
def show_skills(skills):
    """prints skills_list numbered to user"""
    print ("Skills: ")
    skillsA = get_skills()
    for number, skill in enumerate(skillsA, start=1):
        print(number, skill)


# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    """Return a list of the two skills that the user inputted"""
    new_user_list = []
    skillsC = get_skills()
    chosen_number_1 = int(input ("Choose a skill from above by entering its number: "))
    chosen_number_2 = int(input ("Choose another skill from above by entering its number: "))
    new_user_list.append(skillsC[chosen_number_1 -1])
    new_user_list.append(skillsC[chosen_number_2 -1])
    return new_user_list


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
    cv = {
        "skills": get_user_skills(get_skills())
    }
    cv ["name"] = input ("What's your name? ")
    cv ["age"] = input ("How old are you? ")
    cv ["experience"] = input ("How many years of experience do you have? ")
    return cv


# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    # if cv["age"] >25 and <40:
    #     return True


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    ...


if __name__ == "__main__":
    main()
