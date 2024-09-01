class User:
    def __init__(self, first_name, last_name, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        return self.first_name

    def greet_user(self):
        return self.last_name

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(
        self,
    ):
        self.login_attempts = 0
        return self.login_attempts
