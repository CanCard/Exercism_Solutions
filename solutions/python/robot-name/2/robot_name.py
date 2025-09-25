import random, string, secrets

class Robot:
    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):
        random.seed()
        randomLetter = chr(random.randint(ord('A'), ord('Z')))
        randomLetter2 = chr(random.randint(ord('A'), ord('Z')))
        number = ""
        for _ in range(3):
            a = random.randint(0,9)
            number = number + str(a)
        # number = "".join(str(random.randint(0, 9)) for _ in range(3)) --> Bu da kullanılabilirdi daha kısaca.
        self.name = f"{randomLetter}{randomLetter2}{number}"
        return self.name
    
    def reset(self):
        self.name = self.generate_name()