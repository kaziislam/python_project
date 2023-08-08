
def days_to_units(num_of_days, conversation_unit):
    if conversation_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversation_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_numbers = int(days_and_unit_dictionary["days"])
        if user_input_numbers > 0:
            calculated_value = days_to_units(user_input_numbers, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_numbers == 0:
            print("you entered zero, please enter a valid positive number")
        else:
            print("you entered negative number, no conversation would show up")
    except ValueError:
    # else:
        print("input entered is not a number, please try again!")


user_input_message = "Enter number of days and conversation unit!\n"
