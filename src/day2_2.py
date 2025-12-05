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
        for i in range(1, length // 2 + 1):  # +1 is needed to go up to split by the middle
            if length % i == 0 and number_str[:i] * (length // i) == number_str:
                sum_invalid += number
                break

print(sum_invalid)
