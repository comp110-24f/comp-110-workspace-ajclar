"""River Simulation."""

from exercises.ex07.river import River

__author__ = "730807192"

my_river: River = River(10, 2)  # River with 10 fish and 2 bears
my_river.view_river()
my_river.one_river_week()
