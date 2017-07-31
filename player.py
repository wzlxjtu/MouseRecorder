# This program replays the mouse activities recorded by the recorder.py

import win32api
import win32con
import time


# replays according to the log file
with open("data/log_demo.txt") as f:
    for line in f:
        if line[0] != "#":
            operation = line.split(" ")
            time_sleep = float(operation[0])
            x = int(operation[1])
            y = int(operation[2])
            activity = int(operation[3])
            time.sleep(time_sleep)
            if activity == 0:
                win32api.SetCursorPos((x, y))
            if activity == 1:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            if activity == 2:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
            if activity == 3:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
            if activity == 4:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)