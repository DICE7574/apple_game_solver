import cv2
import numpy as np
import mss
import pyautogui
import time

def start_game():
    # 화면 캡처
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        screen = np.array(screenshot)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGRA2BGR)

    threshold = 0.95
    template = cv2.imread(f"img/start.png")

    if template is None:
        print("Template not found")
        return False

    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val < threshold:
        print("Start button not found.")
        return False

    # 버튼 중심 좌표 계산
    t_h, t_w = template.shape[:2]
    center_x = max_loc[0] + t_w // 2
    center_y = max_loc[1] + t_h // 2

    # 클릭후 0.5초 대기
    pyautogui.moveTo(center_x, center_y)
    pyautogui.click()
    print("Clicked start button.")
    time.sleep(0.5)
    return True
