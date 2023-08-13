#import user
from user import User
from post import Post

# create an object from class
app_user_one = User("joe@email.com", "Joe Smith", "Passw0rd", "Software Engineer")
app_user_one.get_user_info()

app_user_one = User("jane@email.com", "Jane Doe", "Passw0rd", "DevOps Engineer")
app_user_one.get_user_info()


app_user_one.change_job_title("DevOps Engineer")
app_user_one.get_user_info()

new_post = Post("Learning Python", app_user_one.name)
new_post.get_post_info()