def does_new_positions_includes_final_position(current_position, grid, prev_position=None):
    (x, y) = current_position
    new_possible_positions = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1)]
    if (3,  3) in new_possible_positions:
        return True

    include_final_position = False
    for p in new_possible_positions:
        if check_if_new_position_available(p, grid, prev_position):
            include_final_position = include_final_position or \
                                     does_new_positions_includes_final_position(p, grid, current_position)

    return include_final_position


def check_if_new_position_available(new_p, grid, prev_position=None):
    (x, y) = new_p
    if (1 <= x <= 3) and (1 <= y <= 3):
        if prev_position and new_p == prev_position:
            return False
        else:
            return grid[x-1][y-1] == "."
    return False


t = int(input())
grid_list = []

for ct in range(t):
    line1 = input()
    line2 = input()
    line3 = input()
    # extra_line = input() if ct < (t-1) else None
    grid_x = []
    for i in range(3):
        col = [line1[i], line2[i], line3[i]]
        grid_x.append(col)
    grid_list.append(grid_x)

start_position = (1, 1)
for g in grid_list:
    if does_new_positions_includes_final_position(start_position, g):
        print("YES")
    else:
        print("NO")


