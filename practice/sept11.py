"""Practice with if-statements and variables, 9.11.24"""


def get_ticket_price() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    elif age > 60:
        price: int = 5
    else:
        price: int = 10
    return price


get_ticket_price()
