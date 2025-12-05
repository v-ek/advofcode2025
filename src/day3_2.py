def get_biggest_joltage_str(line, length):
    # Base case 1: The length we are looking for is the same
    if len(line) == length:
        return "".join([str(i) for i in line])
    # Base case 2: only one digit, just return the max as string
    elif length == 1:
        return str(max(line))
    # Re base case 2: line[:0] returns an empty string
    first_digit = max(line[:-length+1])
    first_index = line.index(first_digit)
    return str(first_digit) + get_biggest_joltage_str(line[first_index+1:], length-1)

# Load data
with open("inputs/day3.txt", "r") as file:
    input = [line.strip() for line in file.readlines()]  

# Setup and preprocess
total_joltage = 0
joltage_length = 12
lines = []
for line in input:
    lines.append([int(char) for char in line])


for line in lines:
    total_joltage += int(get_biggest_joltage_str(line, 12))

print(total_joltage)
