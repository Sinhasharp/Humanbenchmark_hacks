import time
#from selenium import webdriver
#from bs4 import BeautifulSoup
import pyautogui

time.sleep(10)

'''
#set the driver
browser = webdriver.Chrome()


url = "https://humanbenchmark.com/tests/typing"
browser.get(url)

#give some time for the page to fully load
time.sleep(4)

#get the page source
page_source = browser.page_source

#use beautiful soap to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')
spans = soup.find_all('span', class_='incomplete')
text_to_type = ''.join([span.get_text() for span in spans])
print(text_to_type)

#wait for a short time to ensure the webpage is focused
time.sleep(2)'''

#type the text using pyautogui
text_to_type = "So he huffed and he puffed and he blew the house down! The wolf was greedy and he tried to catch both pigs at once, but he was too greedy and got neither! His big jaws clamped down on nothing but air and the two little pigs scrambled away as fast as their little hooves would carry them. The wolf chased them down the lane and he almost caught them. But they made it to the brick house and slammed the door closed before the wolf could catch them."
pyautogui.write(text_to_type, interval=0)