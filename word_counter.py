# TODO:  Accept the user input and clean the input
class CleanInput:
    def __init__(self, user) -> None:
        self.user = user

    def take_input_string(self):
        self.user = input("Enter a sentence of your choice: ")
        return self.user

    def clean_user(self):
        return self.user.lower().strip()
