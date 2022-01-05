import numpy as np
import cv2 as cv
import re
from PIL import Image  # Will need to make sure PIL is installed
import mss
import pyautogui, time
from random import *




#output_filename = 'test.png'
#declare images
button_img = cv.imread('button.png', cv.IMREAD_UNCHANGED)
test_img = cv.imread('test.png', cv.IMREAD_UNCHANGED)
#pyautogui.size()


def screenshot():
	output_filename = 'test.png'
	with mss.mss() as mss_instance:
		monitor_1 = mss_instance.monitors[1]
		screenshot = mss_instance.grab(monitor_1)
		
		img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
		img.save(output_filename, "PNG")  # Save the image





#output_filename = 'test.png'


def match_show():
	pyautogui.write("pls search", 0.1) #18
	pyautogui.press('enter')
	time.sleep(3.0)
	screenshot()
	#print("screenshot taken")
	test_img = cv.imread('test.png', cv.IMREAD_UNCHANGED)


	#cv.imshow('test', test_img)
	#cv.waitKey(0)
	#cv.destroyAllWindows()

	#cv.imshow('button', button_img)
	#cv.waitKey(0)
	#cv.destroyAllWindows()

	result = cv.matchTemplate(test_img, button_img, cv.TM_CCOEFF_NORMED)
	#cv.imshow('Result', result)
	#cv.waitKey()
	#cv.destroyAllWindows()
	min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
	#worst match location, best match location, worst value, best value
	#print(min_val, max_val, min_loc, max_loc)
	#print(max_loc)


########################################################################

	#draw rectangle around match
	w = button_img.shape[1]
	h = button_img.shape[0]

	cv.rectangle(test_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
	#cv.imshow('test', test_img)
	#cv.waitKey(0)
	#cv.destroyAllWindows()


	#print("match analysed")
	threshold = .46
	#result = cv.matchTemplate(test_img, button_img, cv.TM_CCOEFF_NORMED)
	yloc, xloc = np.where(result >= threshold)
	#print(len(xloc))
	#print("coords of rec done")
	if len(xloc) == 0:
		return None
	w = button_img.shape[1]
	h = button_img.shape[0]
	#for (x, y) in zip(xloc, yloc):
	#	cv.rectangle(test_img, (x, y), (x + w, y + h), (0, 255, 255), 2)
	#print("drawn matches")
	rectangles = []
	for (x, y) in zip(xloc, yloc):
		rectangles.append([int(x), int(y), int(w), int(h)])
		rectangles.append([int(x), int(y), int(w), int(h)])
	
	rectangles, weights = cv.groupRectangles(rectangles, 1, 0.2)
#	xc = 1
#	yc = 2
	for (x, y, w, h) in rectangles:
		cv.rectangle(test_img, (x, y), (x + w, y + h), (0, 255, 255), 2)
		#print("making coords")
		xc = x + 34
		yc = y + 28
	
	#xrand = randint(1, 180)     Pick a random number between 1 and 220.
	#xrow = xrand + xc
	#print(xc, yc)

	pyautogui.moveTo(xc, yc)
	pyautogui.click()
	


	#cv.imshow('test', test_img)
	#cv.waitKey(0)

	#print(len(rectangles))



def search_money():
	output_filename = 'test.png'
	pyautogui.size()
	match_show()


#search_money()









