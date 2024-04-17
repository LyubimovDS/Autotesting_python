class User:

    def __init__(self, first_name, last_name):
        self.name = first_name
        self.last_name = last_name

    def print_onli_name(self):
        print(self.name)

    def print_onli_last_name(self):
        print(self.last_name)

    def print_full_name(self):
        print(self.last_name + ' ' + self.name)

