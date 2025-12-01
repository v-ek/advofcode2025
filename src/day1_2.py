with open("inputs/day1.txt", "r") as file:
    input = [line.strip() for line in file.readlines()]

pos = 50
zero_count = 0

for line in input:
    direction = line[0]
    clicks = int(line[1:])
    prev_pos = pos
    if direction == "L":
        # it's still wrong, ahhh
        pos -= clicks
        # We may return to 0 again, but not cross which should add one still
        if pos == 0:
            zero_count += abs(clicks // 100) + 1
        # Or if we come from zero we should subtract one from the num of rotations
        elif pos <= 0:
            zero_count += abs(pos // 100) - int(prev_pos == 0)
    elif direction == "R":
        pos += clicks
        zero_count += pos // 100
    print(f"line: {line}, pos: {pos}, zero_count: {zero_count}")
    pos = pos % 100
# Wrong answers: 6159, 6282, 5832
print(zero_count)
