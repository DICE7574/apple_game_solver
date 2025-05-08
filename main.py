import copy
from apple_detector import detect_apples
from start_game import start_game
from print_grid import print_grid
from solve import solve
from prove import prove
from greedy_answer import greedy_answer

do_solve = True

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

test_grid = copy.deepcopy(grid)
if do_solve:
    solve(grid)
    prove(grid)
greedy_answer(test_grid)