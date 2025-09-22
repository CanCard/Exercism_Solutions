class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        a = self.card_num
        a = a.replace(" ", "")
        for i in a:
            if i.isdigit() == False:
                return False
            
        if not a:
            return False

        if a == "0":
            return False

        a = a[::-1]

        total = 0

        for idx, ch in enumerate(a):
            d = int(ch)

            if idx % 2 == 1:
                doubled = d * 2
                if doubled > 9:
                    doubled -= 9
                total += doubled
            else:
                total += d
            

        return total % 10 == 0

