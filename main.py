from time import sleep, perf_counter
from threading import Thread
import pyautogui, time

def money_an_shit_ig():
	while True:
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
		time.sleep(45.0)

def daily_rewards():
	while True:
		time.sleep(4.0)	
		pyautogui.write("pls daily", 0.1) #18
		pyautogui.press('enter')
		time.sleep(4.0)
		pyautogui.write("owo daily", 0.1) #24
		pyautogui.press('enter')
		time.sleep(4.0)
		pyautogui.write("owo cf all", 0.1)
		pyautogui.press('enter')
		time.sleep(86400.0) #64800.0


start_time = perf_counter()

# create two new threads
t1 = Thread(target=money_an_shit_ig)
t2 = Thread(target=daily_rewards)


#give ya time to run XD
time.sleep(20.0)

# start the threads
while True:
	t1.start()
	t2.start()

# wait for the threads to complete
	t1.join()
	t2.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')