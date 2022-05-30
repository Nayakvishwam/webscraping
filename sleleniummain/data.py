from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
os.environ['PATH'] += r'C:/Users/DELL/Desktop/Websraping/chromedriver_win32'
driver = webdriver.Chrome()
driver.get('https://www.rapidtables.com/calc/math/base-calculator.html')
sumone = driver.find_element_by_id('x')
sumtwo = driver.find_element_by_id('x2')
sumone.send_keys(20)
sumtwo.send_keys(40)
maindata=driver.find_element_by_css_selector('button[onclick="calc()"]')
maindata.click()
