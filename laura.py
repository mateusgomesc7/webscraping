#!/bin/env python3
# Created by atbswp (https://github.com/rmpr/atbswp)
# on 14 Jul 2020 
import pyautogui
import time
import webbrowser
import calendar
pyautogui.FAILSAFE = False

if (__name__ == "__main__"):
  print(calendar.calendar(2020))
  print(calendar.c)


# url = 'https://google.com'
# webbrowser.open(url)
# print(webbrowser.get())
def arvore():
  #wa
  # pyautogui.click(1200, 1030)
  #telegram
  pyautogui.click(1317, 951)
  time.sleep(1)
  for i in range(10):
    pyautogui.typewrite('-'*(10-i))
    pyautogui.typewrite(':star:')
    for j in range(i+1):
      pyautogui.typewrite(':four_leaf_clover:')
    for j in range(i+1):
      if j==i:
        pyautogui.typewrite(':star:')
      else:
        pyautogui.typewrite(':four_leaf_clover:')
    pyautogui.typewrite('-'*(10-i))
    pyautogui.press('enter')
    time.sleep(1)