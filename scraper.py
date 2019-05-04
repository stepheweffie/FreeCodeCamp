from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


options = webdriver.ChromeOptions()
options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://learn.freecodecamp.org/')
wait = WebDriverWait(driver, 15)

modules = driver.find_elements_by_class_name('superblock ')

children = list()
for module in modules:
    print(module.text)
    children.append(module.text)
print(children)

#file = open('first_child.txt', 'w', encoding='UTF-8')
#file.writelines(children[0])

