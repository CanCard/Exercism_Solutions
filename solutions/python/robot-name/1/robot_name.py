import random, string, secrets

class Robot:
    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):
        letters = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(2))
        digits = ''.join(str(secrets.randbelow(10)) for _ in range(3))
        return letters + digits
    
    def reset(self):
        self.name = self.generate_name()