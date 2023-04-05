

def sum(num_list: list) -> int:
    if num_list == []:
        return 0
    return num_list[0] + sum(num_list[1:])


print(sum([1, 2, 3, 4, 5, 6, 7]))


def count(num_list: list) -> int:
    if num_list == []:
        return 0
    return 1 + count(num_list[1:])


print(count([1, 2, 3, 4, 5]))


def find_highest(num_list: list) -> int:
    if len(num_list) == 2:
        return num_list[0] if num_list[0] > num_list[1] else num_list[1]
    sub_max = find_highest(num_list[1:])
    return num_list[0] if num_list[0] > sub_max else sub_max


print(find_highest([1, 8, 234, 5]))
