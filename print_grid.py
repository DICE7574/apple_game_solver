def print_grid(grid):
    count = sum(1 for line in grid for apple in line if apple.num != 0)
    max_columns = max(len(line) for line in grid)
    print()
    print("+" + "-" * (max_columns * 2 - 1) + "+")
    for line in grid:
        row = []
        for apple in line:
            if apple.num == 0:
                row.append(" ")
            else:
                row.append(str(apple.num))

        while len(row) < max_columns:
            row.append(" ")
        print("|" + " ".join(row) + "|")
    print("+" + "-" * (max_columns * 2 - 1) + "+")

    print(f"Remaining Apples: {count}")
