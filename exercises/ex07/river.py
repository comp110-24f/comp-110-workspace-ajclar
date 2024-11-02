"""File to define River class."""

# I thought doc strings go below imports?

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730807192"


class River:
    """River class with bears, fish, and the cycle of life."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Removes fish 3+ years and bears 5+ years old."""
        new_fish: list[Fish] = []
        new_bears: list[Bear] = []
        # Create a new list rather than mutating the active self . list
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.fish = new_fish
        self.bears = new_bears

    def remove_fish(self, amount: int) -> None:
        """Removes the amount of fish."""
        for _ in range(0, amount):
            self.fish.pop(0)  # zero as the lift shifts forward every time

    def bears_eating(self) -> None:
        """If there are more than five fish, the bears eats 3."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)

    def check_hunger(self) -> None:
        """Removes bears with negative hunger scores."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears

    def repopulate_fish(self) -> None:
        """Repopulates fish into the river."""
        num_fish: int = len(self.fish) // 2 * 4
        # For every two fish, four are born
        for _ in range(0, num_fish):
            self.fish.append(Fish())

    def repopulate_bears(self) -> None:
        """Repopulates bears into the river."""
        num_bears: int = len(self.bears) // 2
        # For ever two bears, one bear is born
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def view_river(self):
        """Prints daily river stats."""
        # Uses variable to better organize long print
        to_print: str = f"\n~~~ Day {self.day}: ~~~"
        to_print = to_print + f"\nFish population: {len(self.fish)}"
        to_print = to_print + f"\nBear population: {len(self.bears)}"
        print(to_print)

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """One full week simulation."""
        for _ in range(0, 7):
            self.one_river_day()
