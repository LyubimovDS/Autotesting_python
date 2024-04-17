class Smartphone:
    
    def __init__(self, phone_mark, phone_model, phone_number):
        self.mark = phone_mark
        self.model = phone_model
        self.number = phone_number

    def print_phone(self):
        print(self.mark + " - " + self.model + '. ' + self.number)