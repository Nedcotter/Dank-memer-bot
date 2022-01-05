from time import sleep, perf_counter
from time import gmtime, strftime
import pyautogui, time


def money_an_shit_ig():
	pyautogui.write("pls beg", 0.2)
	pyautogui.press('enter')
	time.sleep(4.0)
	pyautogui.write("pls dig", 0.2)
	pyautogui.press('enter')
	time.sleep(4.0)
	pyautogui.write("pls hunt", 0.2)
	pyautogui.press('enter')
	time.sleep(4.0)
	pyautogui.write("pls fish", 0.2)
	pyautogui.press('enter')


def daily_rewards():
	pyautogui.write("pls daily", 0.1) #18
	pyautogui.press('enter')
	time.sleep(4.0)
	pyautogui.write("owo daily", 0.1) #24
	pyautogui.press('enter')
	time.sleep(4.0)
	pyautogui.write("owo cf all", 0.1)
	pyautogui.press('enter')


def start():
	print("Starting in... 10")
	time.sleep(1.0)
	print("Starting in... 9")
	time.sleep(1.0)
	print("Starting in... 8")
	time.sleep(1.0)
	print("Starting in... 7")
	time.sleep(1.0)
	print("Starting in... 6")
	time.sleep(1.0)
	print("Starting in... 5")
	time.sleep(1.0)
	print("Starting in... 4")
	time.sleep(1.0)
	print("Starting in... 3")
	time.sleep(1.0)
	print("Starting in... 2")
	time.sleep(1.0)
	print("Starting in... 1")
	time.sleep(1.0)


	collected_daily = False
	lasthour = strftime("%H", gmtime())
	daily_rewards()
	while True:
		if collected_daily == False:
			if strftime("%H", gmtime()) == "1":
				print("daily ready")
				daily_rewards()
				collected_daily = True
				print("daily collected")
		if strftime("%H", gmtime()) != "1":
			collected_daily = False

		money_an_shit_ig()
		if autosale == True:
			currenthour = strftime("%H", gmtime())
			if currenthour != lasthour:
				time.sleep(2.0)
				pyautogui.write("pls sell", 0.1) #18
				pyautogui.press('enter')
				from button import confirm
				confirm()
				lasthour = strftime("%H", gmtime())
		if autogift == True:
			currenthour = strftime("%H", gmtime())
			if currenthour != lasthour:
				time.sleep(2.0)
				give = "pls give {} all".format(username)
				pyautogui.write(give, 0.1) #18
				pyautogui.press('enter')
				from button import confirm
				confirm()
				lasthour = strftime("%H", gmtime())
				
				
		time.sleep(4.0)
		from search import search_money
		search_money()
		time.sleep(18.0)


sellitems = input("Would you like to turn on auto sale? (Y/N): ")
#print(sellitems)
if sellitems.lower() == 'y':
	autosale = True
else:
	autosale = False
giftmoney = input("Would you like to turn on auto money transfer? (Y/N): ")
#print(sellitems)
if sellitems.lower() == 'y':
	autogift = True
	username = input("What acc would you like to gift the money to? Format @User#0000 : ")
else:
	autogift = False

start()









































