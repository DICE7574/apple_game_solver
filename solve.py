import pyautogui
from print_grid import print_grid

def drag(left, top, right, bottom):
    pyautogui.moveTo(left - 10, top - 10)
    pyautogui.mouseDown()

    distance = ((right - left + 20) ** 2 + (bottom - top + 20) ** 2) ** 0.5
    pyautogui.moveTo(right + 10, bottom + 10, duration=distance / 200)

    pyautogui.mouseUp()

def solve(grid):
    total_score = 0
    rows = len(grid)
    cols = max(len(row) for row in grid)

    while True:
        found = False

        for y1 in range(rows):
            for y2 in range(y1, rows):
                for x1 in range(len(grid[y1])):
                    for x2 in range(x1, len(grid[y2])):

                        apples_in_area = []
                        for y in range(y1, y2 + 1):
                            for x in range(x1, x2 + 1):
                                if x < len(grid[y]):
                                    apple = grid[y][x]
                                    if apple.num != 0:
                                        apples_in_area.append(apple)

                        total = sum(apple.num for apple in apples_in_area)

                        if total == 10 and apples_in_area:
                            # 드래그 좌표 계산
                            left = min(a.x for a in apples_in_area)
                            top = min(a.y for a in apples_in_area)
                            right = max(a.end_x for a in apples_in_area)
                            bottom = max(a.end_y for a in apples_in_area)

                            # 실제 드래그
                            drag(left, top, right, bottom)

                            # 지우기
                            for apple in apples_in_area:
                                apple.remove()

                            total_score += len(apples_in_area)
                            found = True
                            print_grid(grid)
                            break

                    if found:
                        break
                if found:
                    break
            if found:
                break

        if not found:
            break

    print("Solve finished. Total score:", total_score)
    return total_score