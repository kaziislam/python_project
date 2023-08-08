import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
# print(input_list)
deadline_date = datetime.datetime.strptime(deadline, "%m.%d.%Y")
#print(type(datetime.datetime.strptime(deadline, "%d.%m.%Y")))

# Calculate how many days from now till deadline
print(datetime.datetime.today())
todays_date = datetime.datetime.today()
time_till = deadline_date - todays_date

hours_till = int(time_till.total_seconds() / 60 / 60)
# print(f"Dear user your deadline is: {deadline}! Time remaining for your goal: {goal} is {time_till.days} days")
print(f"Dear user your deadline is: {deadline}! Time remaining for your goal: {goal} is {hours_till} hours")
