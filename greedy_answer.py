def greedy_answer(grid):
    rows = len(grid)
    cols = max(len(row) for row in grid)
    total_score = 0

    while True:
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
                            for apple in apples_in_area:
                                apple.remove()
                            total_score += len(apples_in_area)
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break

        if not found:
            break

    print(f"Greedy Total Score: {total_score}")


    return total_score