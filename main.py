calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    # print(num_of_days > 0)
    condition_check = num_of_days > 0
    # print(type(condition_check))

    if num_of_days > 0:
        return f"{num_of_days} days is {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
    # if user_input.isdigit():
        user_input_numbers = int(num_of_days_element)
        # we want to do conversation only for positive integers
        if user_input_numbers > 0:
            calculated_value = days_to_units(user_input_numbers)
            print(calculated_value)
        elif user_input_numbers == 0:
            print("you entered zero, please enter a valid positive number")
        else:
            print("you entered negative number, no conversation would show up")
    except ValueError:
    # else:
        print("input entered is not a number, please try again!")


user_input = ""
while user_input != "exit":
    user_input = input("Enter number of days as a comma separated list and this application will convert it to hours!\n")
    # print(user_input)
    list_of_days = user_input.split(", ")

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_element in set(list_of_days):
        validate_and_execute()


