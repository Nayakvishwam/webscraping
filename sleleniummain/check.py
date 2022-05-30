import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.common.exceptions import TimeoutException
os.environ['PATH'] += r'C:/Users/DELL/Desktop/Websraping/chromedriver_win32'
driver = webdriver.Chrome()
driver.get('https://www.codewithharry.com/')
# driver.implicitly_wait(30)
# drivermain = webdriver.Chrome()
# drivermain.get('https://github.com/')
# my_elemt = driver.find_element_by_link_text('Courses')
# my_elemt.click()
# my = drivermain.find_element_by_class_name('HeaderMenu-link')
try:
    data =WebDriverWait(driver, 10).until(
        Ec.text_to_be_present_in_element((By.LINK_TEXT, 'Courses'), 'Home!')
    )
    print(data)
except TimeoutError:
    pass
