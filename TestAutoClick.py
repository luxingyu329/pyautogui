"""
Author：L.ZHANG
E-mail: Luxingyu329@163.com
Date：2024/11/4 10:21 
File : TestAutoClick.py
"""
import cv2
import time
import pyautogui

time.sleep(2)  # 首先等2秒 切换界面
# 获取带有房贷计算的屏幕快照保存到本地
image = pyautogui.screenshot()
image.save('Screen.png')
# 基于 cv2读取照片
screen = cv2.imread('Pic_Folder/Screen.png')
joinMeeting = cv2.imread('Pic_Folder/StartCal.png')
# 在屏幕快照中对比开始计算按钮 定位其准确位置
result = cv2.matchTemplate(joinMeeting, screen, cv2.TM_CCOEFF_NORMED)
# result 是一个二维列表，列表中最大值元素的位置就是我们对比后相似度最高的图片【左上角】位置
print(result)

# minMaxLoc 返回一个元组，其中三个元素，以此为最不相似点分数，最相似点分数，最不相似点位置坐标，最相似点位置坐标
pos_start = cv2.minMaxLoc(result)[3]  # 获得最相似点相似坐标
print(pos_start)
# x = pos_start[0]
# y = pos_start[1]

# 定位到点击图片的中间位置
x = pos_start[0] + int(joinMeeting.shape[1] / 2)
y = pos_start[1] + int(joinMeeting.shape[0] / 2)

# 暂停1秒后开始点击
time.sleep(1)
pyautogui.click(x, y, button='left')
