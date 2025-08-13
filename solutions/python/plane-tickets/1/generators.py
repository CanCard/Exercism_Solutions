"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    m = ["A","B","C","D"]
    i = 0
    while i < number:
        yield m[i%4]
        i+=1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    generated_seats = generate_seat_letters(number)
    row = 0
    for seat in generated_seats:
        if seat == 'A':
            row += 1
        if row == 13:
            row += 1
        yield str(row) + seat
        
    

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    returning = {}
    
    messi = generate_seats(len(passengers))
    for passenger in passengers:
        returning[passenger] = next(messi)

    return returning

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    one,two,three,four = seat_numbers[0],seat_numbers[1],seat_numbers[2],seat_numbers[3]
    trophy = one+flight_id
    trophy2 = two+flight_id
    trophy3 = three+flight_id
    trophy4 = four+flight_id
    trophy_list = [trophy,trophy2,trophy3,trophy4]
    
    for i in trophy_list:
        messi = 12 - len(i)
        yield i + "0"*messi

    """SHORT ANSWER
    
    for seat in seat_numbers:
        base_string = f'{seat}{flight_id}'
        yield base_string + '0' * (12 - len(base_string))"""