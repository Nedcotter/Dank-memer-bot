import numpy as np
import cv2 as cv
import re
from PIL import Image  # Will need to make sure PIL is installed
import mss
import pyautogui, time


output_filename = 'test.png'
#declare images
share_img = cv.imread('share.png', cv.IMREAD_UNCHANGED)
#test_img = cv.imread('test.png', cv.IMREAD_UNCHANGED)
pyautogui.size()


def screenshot():
	output_filename = 'test.png'
	with mss.mss() as mss_instance:
		monitor_1 = mss_instance.monitors[1]
		screenshot = mss_instance.grab(monitor_1)
		
		img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
		img.save(output_filename, "PNG")  # Save the image



def test_feed():
#	cv.imshow('test', test_img)
	cv.waitKey(0)
	cv.destroyAllWindows()

#	cv.imshow('share', share_img)
	cv.waitKey(0)
	cv.destroyAllWindows()

def match_heat():
	test_img = cv.imread('test.png', cv.IMREAD_UNCHANGED)
	result = cv.matchTemplate(test_img, share_img, cv.TM_CCOEFF_NORMED)
#	cv.imshow('Result', result)
#	cv.waitKey()
#	cv.destroyAllWindows()
	min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
	#worst match location, best match location, worst value, best value
	#print(min_val, max_val, min_loc, max_loc)
	print(max_loc)

def loc_match():
	#draw rectangle around match
	w = share_img.shape[1]
	h = share_img.shape[0]

	cv.rectangle(test_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
#	cv.imshow('test', test_img)
	cv.waitKey(0)
	cv.destroyAllWindows()


#output_filename = 'test.png'


def match_show():
	pyautogui.write("pls give "+ str(username) + "all", 0.1)
	pyautogui.press('enter')
	time.sleep(3.0)
	screenshot()
	time.sleep(2.0)
	test_img = cv.imread('test.png', cv.IMREAD_UNCHANGED)
#	test_feed()
	match_heat()
	#loc_match()
	threshold = .60
	result = cv.matchTemplate(test_img, share_img, cv.TM_CCOEFF_NORMED)
	yloc, xloc = np.where(result >= threshold)
#	print(len(xloc))
	w = share_img.shape[1]
	h = share_img.shape[0]
	#for (x, y) in zip(xloc, yloc):
	#	cv.rectangle(test_img, (x, y), (x + w, y + h), (0, 255, 255), 2)
	
	rectangles = []
	for (x, y) in zip(xloc, yloc):
		rectangles.append([int(x), int(y), int(w), int(h)])
		rectangles.append([int(x), int(y), int(w), int(h)])
	
	rectangles, weights = cv.groupRectangles(rectangles, 1, 0.2)
	
	for (x, y, w, h) in rectangles:
		cv.rectangle(test_img, (x, y), (x + w, y + h), (0, 255, 255), 2)
		xa = x + 3
		ya = y + 2
#	print(xa, ya)
	pyautogui.moveTo(xa, ya)
	pyautogui.click()
	


#	cv.imshow('test', test_img)
#	cv.waitKey(0)

#	print(len(rectangles))



def share():
	match_show()