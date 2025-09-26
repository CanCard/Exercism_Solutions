import re

def clean(number):
    number = ''.join(re.findall(r'[^+()\-\s\.]+', number))
    return number

class PhoneNumber:
    def __init__(self, number):
        
        number = clean(number)
        
        # if a phone number has less than 10 digits.
        if number.isdigit() and len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")

        # if a phone number has more than 11 digits.
        elif number.isdigit() and len(number) > 11:
            raise ValueError("must not be greater than 11 digits")

        # if a phone number has 11 digits, but starts with a number other than 1.
        elif len(number) == 11:
            if number.isdigit() and number[0] != '1':
                raise ValueError("11 digits must start with 1")
            else:
                number = number[1:]
                
        area_code = number[:3]
        exchange_code = number[3:6]
        subscriber_number = number[6:]
        
        # if a phone number has an exchange code that starts with 0.
        if exchange_code[0] == '0':
            raise ValueError("exchange code cannot start with zero")

        # if a phone number has an exchange code that starts with 1.
        elif exchange_code[0] == '1':
            raise ValueError("exchange code cannot start with one")

        # if a phone number has an area code that starts with 0.
        elif area_code[0] == '0':
            raise ValueError("area code cannot start with zero")

        # if a phone number has an area code that starts with 1.
        elif area_code[0] == '1':
            raise ValueError("area code cannot start with one")

        # if a phone number has punctuation in place of some digits.
        elif re.search(r'\W+', number):
            raise ValueError("punctuations not permitted")

        # if a phone number has letters in place of some digits.
        elif re.search(r'[a-zA-Z]+', number):
            raise ValueError("letters not permitted")
            
        self.number = number
        self.area_code = area_code
        self.exchange_code = exchange_code
        self.subscriber_number = subscriber_number
                
    def pretty(self):
        return f'({self.area_code})-{self.exchange_code}-{self.subscriber_number}'