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
    #print(module.text)
    children.append(module.text)
#print(children)

#file = open('first_child.txt', 'w', encoding='UTF-8')
#file.writelines(children[0])

read_file = open('first_child.txt', 'r', encoding='UTF-8')
read_lines = read_file.readlines()
for line in read_lines[:3]:
    # Omit \n from dir name
    line = line[:-2]
    os.mkdir(line)
    os.chdir(line)
for ex in read_lines[3:]:
    if ex != "Not Passed\n":
        # Omit 'Not Passed\n' and '\n'
        ex = ex[11:-2]
        #ex_file = open(ex + '.html', 'w', encoding='UTF-8')
        print(ex)