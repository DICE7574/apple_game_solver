from apple_detector import detect_apples
from start_game import start_game
from print_grid import print_grid
from solve import solve

if start_game():
    print("Game started.")
else:
    print("Failed to start the game.")
    exit(1)

grid = detect_apples()

if grid is None:
    print("Game start failed. Exiting.")
    exit()
else:
    print_grid(grid)

solve(grid)