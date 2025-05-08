import pyautogui
from print_grid import print_grid

def drag(left, top, right, bottom):
    pyautogui.moveTo(left - 10, top - 10)
    pyautogui.mouseDown()

    distance = ((right - left + 20) ** 2 + (bottom - top + 20) ** 2) ** 0.5
    pyautogui.moveTo(right + 10, bottom + 10, duration=distance / 200)

    pyautogui.mouseUp()

def find_removable_groups(grid):
    rows = len(grid)
    candidates = []
    for y1 in range(rows):
        for x1 in range(len(grid[y1])):
            for y2 in range(y1, rows):
                for x2 in range(x1, len(grid[y2])):
                    apples_in_area = []
                    for y in range(y1, y2 + 1):
                        for x in range(x1, x2 + 1):
                            if x < len(grid[y]):
                                apple = grid[y][x]
                                if apple.num != 0:
                                    apples_in_area.append(apple)

                    total = sum(apple.num for apple in apples_in_area)
                    if total > 10:
                        break
                    if total == 10 and apples_in_area:
                        # 후보로 저장
                        candidates.append(apples_in_area)
    return candidates

def solve(grid):
    total_score = 0
    while True:
        candidates = find_removable_groups(grid)

        if not candidates:
            break

        selected = min(candidates, key=lambda group: (len(group), -max(a.num for a in group)))

        # 드래그 좌표 계산
        left = min(a.x for a in selected)
        top = min(a.y for a in selected)
        right = max(a.end_x for a in selected)
        bottom = max(a.end_y for a in selected)

        # 실제 드래그
        drag(left, top, right, bottom)

        # 지우기
        for apple in selected:
            apple.remove()

        total_score += len(selected)
        print_grid(grid)

    print("Solve finished. Total score:", total_score)
    return total_score