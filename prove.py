from print_grid import print_grid

def prove(grid):
    rows = len(grid)
    found = False

    for y1 in range(rows):
        for x1 in range(len(grid[y1])):
            for y2 in range(y1, rows):
                for x2 in range(x1, len(grid[y2])):

                    apples_in_area = []
                    total = 0
                    for y in range(y1, y2 + 1):
                        for x in range(x1, x2 + 1):
                            if x < len(grid[y]):
                                apple = grid[y][x]
                                if apple.num != 0:
                                    apples_in_area.append(apple)
                                    total += apple.num

                    if total == 10 and apples_in_area:
                        print("Found removable group:")
                        print([a.num for a in apples_in_area])
                        found = True

    if not found:
        print("No removable groups left. This grid is clean.")
    else:
        print("There are still removable groups left!")