"""
Author：L.ZHANG
E-mail: Luxingyu329@163.com
Date：2024/11/4 9:04
File : TestPyautogui.py
"""
import time

import cv2
import pyautogui

print(pyautogui.size())

width, height = pyautogui.size()
print(width, height)

# 测试移动鼠标 （从屏幕中间开始画一个正方形）
# pyautogui.moveTo(width/2, height/2, duration=0.25)
# pyautogui.moveTo(width/2, height/2+100, duration=0.25)
# pyautogui.moveTo(width/2-100, height/2+100, duration=0.25)
# pyautogui.moveTo(width/2-100, height/2, duration=0.25)
# pyautogui.moveTo(width/2, height/2, duration=0.25)

# for _ in range(5):  # 画 5次
#     # 利用绝对坐标  测试移动鼠标 （从屏幕中间开始画一个正方形）
#     pyautogui.moveTo(width / 2, height / 2, duration=0.25)
#     pyautogui.moveTo(width / 2, height / 2 + 100, duration=0.25)
#     pyautogui.moveTo(width / 2 - 100, height / 2 + 100, duration=0.25)
#     pyautogui.moveTo(width / 2 - 100, height / 2, duration=0.25)
#     pyautogui.moveTo(width / 2, height / 2, duration=0.25)

# for _ in range(5):
#     # 利用相对对坐标  测试移动鼠标 （从当前鼠标位置开始画一个正方形）
#     pyautogui.moveRel(300, 0, duration=0.25)
#     pyautogui.moveRel(0, 300, duration=0.25)
#     pyautogui.moveRel(-300, 0, duration=0.25)
#     pyautogui.moveRel(0, -300, duration=0.25)

# 获取鼠标位置
current_p = pyautogui.position()
print(current_p)
x, y = pyautogui.position()
print(x, y)

# 鼠标点击
# pyautogui.click()  # 默认当前位置，也可以传入参数 x, y

# 右键点击
# pyautogui.click(500,500, button='right')

# 拖动鼠标
# time.sleep(2)  # 为了等待就位
# pyautogui.click()
# length = 80
# while length > 0:
#     pyautogui.dragRel(length, 0, duration=0.25, button='left')
#     length -= 5
#     pyautogui.dragRel(0, length, duration=0.25, button='left')
#     pyautogui.dragRel(-length, 0, duration=0.25, button='left')
#     length -= 5
#     pyautogui.dragRel(0, -length, duration=0.25, button='left')

# image = pyautogui.screenshot()
# image.save('Pic_Folder/Screen.png')  # 不要有中文

image = pyautogui.screenshot()  # 获取屏幕快照
print(image.getpixel((329, 329)))  # 打印坐标像素值
result = pyautogui.pixelMatchesColor(329, 329, (49, 51, 53))  # 与像素值进行比较
print(result)  # 输出返回的比较结果

