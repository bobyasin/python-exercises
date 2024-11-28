def find_max(numbers: list[int]):
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number

    return max_number