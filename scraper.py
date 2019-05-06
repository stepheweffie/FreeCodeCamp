from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import os

options = webdriver.ChromeOptions()
options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://learn.freecodecamp.org/')
wait = WebDriverWait(driver, 15)

children = list()
file = open('first_child.txt', 'w', encoding='UTF-8')


def write_element_text(element):
    p = 'Projects'
    h = '(300 hours)'
    new_text = str()
    if p in element.text:
        n = p + '\n'
        new_text = str(element.text).replace(p, n)
    elif h in element.text:
        new_text = '\n' + element.text
    else:
        children.append(element.text)
        return file.writelines(element.text)
    file.writelines(new_text)
    children.append(new_text)


elements = driver.find_elements_by_class_name('superblock ')
for elem in elements[-6:]:
    write_element_text(elem)
    elem.click()

elements = driver.find_elements_by_class_name('block ')
for elem in elements:
    #write_element_text(elem)
    elem.click()

elements = driver.find_elements_by_class_name('superblock ')
#elements = driver.find_elements_by_class_name('map-challenge-title')
for elem in elements:
    write_element_text(elem)

file.close()


def iterate(line):
    if '(300 hours)' or 'Interview' in line:
        module_dir = line[:-1]
        os.mkdir(module_dir)
        os.chdir(module_dir)
    elif "Not Passed" in line:
        # Omit 'Not Passed\n' and '\n'
        if line != "Not Passed\n":
            if line[-1] == '\n':
                line = line[10:-1]
            else:
                line = line[10:]
            ex_file = open(line + '.html', 'w', encoding='UTF-8')
            ex_file.close()
    else:
        os.mkdir(line[:-1])
        os.chdir(line[:-1])


def fcc_curriculum():

    read_file = open('first_child.txt', 'r', encoding='UTF-8')
    read_lines = read_file.readlines()
    try:
        for lines in read_lines[:3]:
            # Omit \n from dir name
            l = lines[:-1]
            os.mkdir(l)
            os.chdir(l)

        for lines in read_lines[3:]:
            for child in children[0]:
                if lines in child:
                        #child = child
                        iterate(lines)
        os.chdir('..')
        os.chdir('..')
        for lines in read_lines[3:]:
            for child in children[1:]:
                if lines in child:
                    iterate(lines)
                    if lines == child[-len(lines):] or lines == child[:len(lines)]:
                        os.chdir('..')
        file.close()

    except FileExistsError:
        pass
