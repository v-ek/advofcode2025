with open("inputs/day3.txt", "r") as file:
    input = [line.strip() for line in file.readlines()]  

total_joltage = 0
lines = []
for line in input:
    lines.append([int(char) for char in line])

for line in lines:
    first_digit = max(line[:-1])
    first_index = line.index(first_digit)
    second_digit = max(line[first_index+1:])
    joltage = int(str(first_digit) + str(second_digit))
    total_joltage += joltage

print(total_joltage)
