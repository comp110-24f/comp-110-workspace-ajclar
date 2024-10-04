def view(my_list: list[int]):
    idx: int = 0
    while idx < len(my_list):
        print(my_list[idx])
        idx += 1


msg: list[int] = ["Hello", "World"]
view(msg)
print(msg)
