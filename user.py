# class definition
class User:
    # __init__ function
    def __init__(self, email, name, password, current_job_title):
        # constructor
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    # following are the methods
    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact at {self.email}")

