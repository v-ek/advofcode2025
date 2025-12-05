def compute_neighborhood(coordinates: tuple[int, int], max_x: int, max_y: int):
    neighborhood = set()
    neighbors = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1), 
        (1, -1),
        (1, 0), 
        (1, 1), 
    )
    for d_x, d_y in neighbors:
        new_coord = (coordinates[0] + d_x, coordinates[1] + d_y)
        if new_coord[0] < 0 or new_coord[0] > max_x or new_coord[1] < 0 or new_coord[1] > max_y:
            continue
        else:
            neighborhood.add(new_coord)
    return neighborhood


# Load data
with open("inputs/day4.txt", "r") as file:
    input = [line.strip() for line in file.readlines()]  

locations_w_neighborhoods = {}
num_removed = 0
taken_coordinates = set()

# Coordinate system = x steps to the right, y = steps down
# First pass, build set of all taken locations + list of tuples of coordinates and neighborhoods
for row_index in range(depth := len(input)):
    curr_digits = []
    curr_number_coordinates = []
    line = input[row_index]
    for col_index in range(width := len(line)): 
        curr_coordinates = (col_index, row_index)
        if input[row_index][col_index] == "@":
            taken_coordinates.add((col_index, row_index))
            neighborhood = compute_neighborhood(curr_coordinates, width, depth)
            locations_w_neighborhoods[curr_coordinates] = neighborhood

# Second pass: Remove all that can be removed, start over until all have 4 or more neighbors
while True:
    removed_last_round = set()
    for curr_coordinates, neighborhood in locations_w_neighborhoods.items():
        if len(neighborhood.intersection(taken_coordinates)) < 4:
            num_removed += 1
            removed_last_round.add(curr_coordinates)
    taken_coordinates -= removed_last_round
    for curr_coordinates in removed_last_round:
        del locations_w_neighborhoods[curr_coordinates]
    if not removed_last_round:
        break

print(num_removed)
