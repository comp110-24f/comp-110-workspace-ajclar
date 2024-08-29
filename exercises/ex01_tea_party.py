"""Calculates the needed amount of food and cost for a tea party."""

__author__ = "730807192"


def main_planner(guests: int) -> None:
    """Run the program, calculating tea part cost based of # of guests."""
    # Using variables would be so nice here haha
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    # Below, one singular line threw an error - better formatting fixed it.
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculate the needed # of tea bags."""
    return people * 2


def treats(people: int) -> int:
    """Calculate the needed # of treats."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost of the tea party."""
    return float((tea_count * 0.5) + (treat_count * 0.75))


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
