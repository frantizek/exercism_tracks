class PhoneNumber:
    def __init__(self, number):

        # if a phone number has punctuation in place of some digits.
        # if any([c in ",.;:!()[]{}<>?@#%^&*-_=+~\\/|\"'" for c in number]):
        if any([c in "@:!" for c in number]):            
            raise ValueError("punctuations not permitted")
        
        number = "".join([c for c in number if c.isalnum()])
        # print(f" number = {number} and is {len(number)} characters long")

        
        # if a phone number has less than 10 digits.
        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        
        # if a phone number has more than 11 digits.
        if len(number) > 11:
            raise ValueError("must not be greater than 11 digits")
        
        # if a phone number has 11 digits, but starts with a number other than 1.
        if len(number) == 11 and number[0] != "1":
            raise ValueError("11 digits must start with 1")

        if len(number) == 11 and number[0] == "1":
            number = number[1:]
        
        # if a phone number has an exchange code that starts with 0.
        if len(number) == 10 and number[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        
        # if a phone number has an exchange code that starts with 1.
        if len(number) == 10 and number[3] == "1":
            raise ValueError("exchange code cannot start with one")
        
        # if a phone number has an area code that starts with 0.
        if len(number) == 10 and number[0] == "0":
            raise ValueError("area code cannot start with zero")
        
        # if a phone number has an area code that starts with 1.
        if len(number) == 10 and number[0] == "1":
            raise ValueError("area code cannot start with one")
        
        # if a phone number has punctuation in place of some digits.
        # if any([c in ",.;:!()[]{}<>?@#%^&*-_=+~\\/|\"'" for c in number]):
        if any([c in "@:!" for c in number]):            
            raise ValueError("punctuations not permitted")
        
        # if a phone number has letters in place of some digits.
        if any([c for c in number if c.isalpha()]):
            raise ValueError("letters not permitted")

        self.number = number

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"

    @property
    def area_code(self):
        return self.number[:3]