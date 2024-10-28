"""Helpful dictionary util with a story!"""

__author__ = "730807192"


def invert(toInvert: dict[str, str]) -> dict[str, str]:
    """Returns inverted key/value pairs of the dictionary."""
    inverted: dict[str, str] = {}
    for key in toInvert:
        if not (toInvert[key] in inverted):
            inverted[toInvert[key]] = key
        else:
            raise KeyError("Cannot have duplicate keys!")
    return inverted


def favorite_color(fav_colors: dict[str, str]) -> str:
    """Returns the value of the dictionary that is present the most."""
    color_counts: dict[str, int] = {}
    fav_color: str = ""
    for key in fav_colors:
        color: str = fav_colors[key]
        if (
            color in color_counts
        ):  # key in dict!! - tried to do: if not (color_counts[color])
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    for color in color_counts:
        if fav_color == "":
            fav_color = color
        elif color_counts[color] > color_counts[fav_color]:
            fav_color = color
    return fav_color


def count(to_anaylze: list[str]) -> dict[str, int]:
    """Counts the number of unique values in a list."""
    counts: dict[str, int] = {}
    for value in to_anaylze:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts


def alphabetizer(my_list: list[str]) -> dict[str, list[str]]:
    """Returns a dict that alphabetized a list of words."""
    sorted: dict[str, list[str]] = {}
    for word in my_list:
        letter: str = word[0].lower()
        # originally .lower()'ed the word, but better to skip to the letter
        if letter in sorted:
            sorted[letter].append(word)
        else:
            sorted[letter] = [word]
    return sorted


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Handle student attendance by day of the week."""
    if day in attendance:
        if not (student in attendance[day]):  # Don't repeat students!
            attendance[day].append(student)
    else:
        attendance[day] = [student]
