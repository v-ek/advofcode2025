with open("inputs/day2.txt", "r") as file:
    input = [line.strip() for line in file.readlines()][0]

ranges = input.split(",")

sum_invalid = 0
for entry in ranges:
    start, end = [int(e) for e in entry.split("-")]
    numbers = range(start, end+1)

    for number in numbers:
        number_str = str(number)
        length = len(number_str)
        if number_str[length//2:] == number_str[:length//2:]:
            print(f"{number_str} vas invalid")
            sum_invalid += number

print(sum_invalid)
