# Load data
with open("inputs/day5_test.txt", "r") as file:
    input = [line.strip() for line in file.readlines()]  

pairs = []
num_fresh = 0
for index, line in enumerate(input):
    if not line:
        first_available_line_index = index + 1
        break
    start_str, end_str = line.split("-")
    pairs.append((int(start_str), int(end_str)))

for line in input[first_available_line_index:]:
    for pair in pairs:
        if int(line) > pair[0] and int(line) <= pair[1]:
            num_fresh += 1
            break

print(num_fresh)
