def get_voters(min_age: int, voters_age: list[int]) -> int:
    count: int = 0
    for x in voters_age:
        if x >= min_age:
            count += 1
    return count


print(get_voters(18, [12, 13, 17]))
print(get_voters(18, [12, 23, 17]))


def test_get_voters() -> None:
    assert get_voters(18, [12, 13, 17]) == 0


test_get_voters()
