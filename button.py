import numpy as np
import cv2 as cv
import re
from PIL import Image  # Will need to make sure PIL is installed
import mss
import pyautogui, time
from random import *
import ctypes
user32 = ctypes.windll.user32\
#screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
middle = round(user32.GetSystemMetrics(0) / 4)
height = round(user32.GetSystemMetrics(1))
half = round(user32.GetSystemMetrics(0) / 2)


#output_filename = 'test.png'
#declare images
confirm_img = cv.imread('confirm.png', cv.IMREAD_UNCHANGED)
test_img = cv.imread('test.png', cv.IMREAD_UNCHANGED)
#pyautogui.size()


def screenshot():

	output_filename = 'test.png'
	with mss.mss() as mss_instance:
		rect = {"left": middle, "top": 300, "width": half, "height": height}
		monitor_1 = mss_instance.monitors[1]
		screenshot = mss_instance.grab(rect)
		
		img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
		img.save(output_filename, "PNG")  # Save the image





#output_filename = 'test.png'


def match_show():

	time.sleep(3.0)
	screenshot()
	time.sleep(3.0)
	#print("screenshot taken")
	confirm_img = cv.imread('confirm.png', cv.IMREAD_UNCHANGED)
	test_img = cv.imread('test.png', cv.IMREAD_UNCHANGED)


	#cv.imshow('test', test_img)
	#cv.waitKey(0)
	#cv.destroyAllWindows()

	#cv.imshow('confirm', confirm_img)
	#cv.waitKey(0)
	#cv.destroyAllWindows()

	result = cv.matchTemplate(test_img, confirm_img, cv.TM_CCOEFF_NORMED)
	#cv.imshow('Result', result)
	#cv.waitKey()
	#cv.destroyAllWindows()
	min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
	#worst match location, best match location, worst value, best value
	#print(min_val, max_val, min_loc, max_loc)
	#print(max_loc)


########################################################################

	#draw rectangle around match
	w = confirm_img.shape[1]
	h = confirm_img.shape[0]

	cv.rectangle(test_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
	#cv.imshow('test', test_img)
	#cv.waitKey(0)
	#cv.destroyAllWindows()


	#print("match analysed")
	threshold = .35
	#result = cv.matchTemplate(test_img, confirm_img, cv.TM_CCOEFF_NORMED)
	yloc, xloc = np.where(result >= threshold)
	#print(len(xloc))
	#print("coords of rec done")
	if len(xloc) == 0:
		return None
	w = confirm_img.shape[1]
	h = confirm_img.shape[0]
	#for (x, y) in zip(xloc, yloc):
	#	cv.rectangle(test_img, (x, y), (x + w, y + h), (0, 255, 255), 2)
	#print("drawn matches")
	rectangles = []
	for (x, y) in zip(xloc, yloc):
		rectangles.append([int(x), int(y), int(w), int(h)])
		rectangles.append([int(x), int(y), int(w), int(h)])
	#print(rectangles)	
	rectangles, weights = cv.groupRectangles(rectangles, 1, 0.2)
#	xc = 3
#	yc = 2
	for (x, y, w, h) in rectangles:
		cv.rectangle(test_img, (x, y), (x + w, y + h), (0, 255, 255), 2)
		print("making coords")
		xc = x + 3
		yc = y + 2
	
	#xrand = randint(1, 180)     Pick a random number between 1 and 220.
	#xrow = xrand + xc
	print(x, y)
	pressx = x + middle
	pressy = y + 300
	pyautogui.moveTo(pressx, pressy)
	#pyautogui.click()
	


	#cv.imshow('test', test_img)
	#cv.waitKey(0)

	#print(len(rectangles))



def confirm():
	output_filename = 'test.png'
	pyautogui.size()
	match_show()



