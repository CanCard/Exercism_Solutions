YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def score(dice, category):
    # Amaç kategorilerin skorlarını döndürmek.. Her bir kategori için skor döndür.. Olayın bu kadar.
    ones_score = sum(d for d in dice if d == 1)
    twos_score = sum(d for d in dice if d == 2)
    threes_score = sum(d for d in dice if d == 3)
    fours_score = sum(d for d in dice if d == 4)
    fives_score = sum(d for d in dice if d == 5)
    sixes_score = sum(d for d in dice if d == 6)

    dice_dict = {}

    for d in dice:
        if d in dice_dict:
            dice_dict[d] += 1
        else:
            dice_dict[d] = 1

    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    elif category == ONES:
        return ones_score
    elif category == TWOS:
        return twos_score
    elif category == THREES:
        return threes_score
    elif category == FOURS:
        return fours_score
    elif category == FIVES:
        return fives_score
    elif category == SIXES:
        return sixes_score
    elif category == CHOICE:
        return sum(dice)
    elif category == LITTLE_STRAIGHT:
        if len(set(dice)) == 5 and (6 not in dice):
            return 30
    elif category == BIG_STRAIGHT:
        if len(set(dice)) == 5 and (1 not in dice):
            return 30
    elif category == FOUR_OF_A_KIND:
        for key, value in dice_dict.items():
            if value >= 4:
                return key*4
    elif category == FULL_HOUSE:
        if len(set(dice)) == 2:
            for key, value in dice_dict.items():
                if value == 3:
                    return sum(dice)
    
    return 0