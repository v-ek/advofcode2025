with open("inputs/day1.txt", "r") as file:
    input = [line.strip() for line in file.readlines()]

pos = 50
zero_count = 0

for line in input:
    direction = line[0]
    clicks = int(line[1:])
    if direction == "L":
        pos = (pos - clicks) % 100
    elif direction == "R":
        pos = (pos + clicks) % 100
    if pos == 0:
        zero_count += 1

print(zero_count)
