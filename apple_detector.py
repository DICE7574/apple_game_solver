import cv2
import numpy as np
import mss

class Apple:
    def __init__(self, num, x, y, w, h):
        self.num = num
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.end_x = x + w
        self.end_y = y + h

    def remove(self):
        self.num = 0

def detect_apples():
    # 화면 캡처
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        screen = np.array(screenshot)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGRA2BGR)

    threshold = 0.95
    detected_apples = []

    for num in range(1, 10):
        template = cv2.imread(f"img/apple{num}.png")
        if template is None:
            continue

        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)

        for pt in zip(*loc[::-1]):
            new_apple = Apple(num, pt[0], pt[1], template.shape[1], template.shape[0])

            # 중복 제거
            size = 20
            if any(abs(new_apple.x - exist.x) < size and abs(new_apple.y - exist.y) < size for exist in detected_apples):
                continue
            detected_apples.append(new_apple)

    # 줄 나누기
    lines = []
    y_threshold = 40

    for apple in detected_apples:
        for line in lines:
            if abs(line[0].y - apple.y) < y_threshold:
                line.append(apple)
                break
        else:
            lines.append([apple])

    # 줄 내부 X 정렬, 줄 자체 Y 정렬
    for line in lines:
        line.sort(key=lambda a: a.x)
    lines.sort(key=lambda line: line[0].y)

    # 2차원 숫자 배열 생성
    grid = [[apple for apple in line] for line in lines]

    total_apples = sum(len(line) for line in grid)
    row_count = len(grid)
    column_count = max((len(line) for line in grid), default=0)

    print("\n=== Grid Info ===")
    print(f"Total apples: {total_apples}")
    print(f"Columns (width): {column_count}")
    print(f"Rows (height): {row_count}")
    print("=================\n")

    if column_count == 17 and row_count == 10 and total_apples == 170:
        return grid
    else:
        print("Detection failed")
        return None
