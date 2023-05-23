def print_even(numbers):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    for num in numbers:
        if num % 2 == 0:
            print(num)


new_nums = [12, 123, 54, 23, 65, 86, 34, 1267, 21]

print_even(new_nums)