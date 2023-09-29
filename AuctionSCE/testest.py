def digit_sum(num):
    total = 0
    while num != 0:
        total += num % 10
        num //= 10
    return total


def print_numbers(num):
    printed_numbers = []
    summation = 0

    for i in range(1, num + 1):
        if i % 5 == 0 or i % 7 == 0:
            if digit_sum(i) <= 6:
                print(i, end=" ")
                printed_numbers.append(i)
                summation += i

    print("\n------------------------------")
    if len(printed_numbers) == 0:
        print("\nThe summation of the printed integers is", summation)
        print("No number printed")
    else:
        print("\nThe summation of the printed integers is", summation)


if __name__ == '__main__':
    digit_sum(54321)
    # user_input = int(input("Enter an integer number: "))
    # print_numbers(user_input)