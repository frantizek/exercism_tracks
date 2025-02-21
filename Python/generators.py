"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    # count = 1
    # seat_index = 0
    # seat_letters = ["A", "B", "C", "D"]
    # while count <= number:
    #     yield seat_letters[seat_index]
    #     count += 1
    #     if seat_index >= 3:
    #         seat_index = 0
    #     else:
    #         seat_index += 1

    seat_letters = ["A", "B", "C", "D"]
    for i in range(number):
        yield seat_letters[i % len(seat_letters)]



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
    total_seats = number + 1 if number >= 13 else number
    seat_letter = generate_seat_letters(number)
    seat_rows = 1
    for seat in range(number):
        yield str(seat_rows) + next(seat_letter, " ")
        if (seat+1) % 4 == 0:
            if seat_rows + 1 == 13:
                seat_rows += 2
            else:
                seat_rows += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    total_number_passengers = len(passengers)
    passengers_with_seats = {}
    seat = generate_seats(total_number_passengers)
    for passenger in passengers:
        passengers_with_seats[passenger] = next(seat, " ")
    return passengers_with_seats

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat_number in seat_numbers:
        yield f"{seat_number}{flight_id}{'0'*(12 - len(seat_number) - len(flight_id))}"
