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

elements = driver.find_elements_by_class_name('superblock ')
#elements = driver.find_elements_by_tag_name('li')
children = list()

for element in elements[-6:]:
    #children.append(element.text)
    element.click()

file = open('first_child.txt', 'w', encoding='UTF-8')
for element in elements:
    #print(module.text)
    p = 'Projects'
    if p in element.text:
        n = p + '\n'
        new_text = str(element.text).replace(p, n)
        file.writelines(new_text)
    else:
        file.writelines(element.text)

#print(children)
file.close()
read_file = open('first_child.txt', 'r', encoding='UTF-8')
read_lines = read_file.readlines()
#print("reading lines")
try:
    for line in read_lines[:3]:
        # Omit \n from dir name
        l = line[:-1]
        os.mkdir(l)
        os.chdir(l)
        #print("changing dirs")
        if line == read_lines[0]:
            for mod in read_lines[-7:]:
                if mod[-1] == '\n':
                    mod_dir = mod[:-1]
                    os.mkdir(mod_dir)
                else:
                    os.mkdir(mod)
                #print("making a dir")
    for ex in read_lines[3:]:
        if ex != "Not Passed\n":
            # Omit 'Not Passed\n' and '\n'
            if "Not Passed" in ex:
                if ex[-1] == '\n':
                    ex = ex[10:-1]
                else:
                    ex = ex[10:]
                ex_file = open(ex + '.html', 'w', encoding='UTF-8')

except FileExistsError:
    pass

clicks = list()
click = wait.until(EC.element_to_be_clickable((By.XPATH,
                                               '//*[@id="___gatsby"]/div/main/div/div[4]/ul/li[1]/ul/li[2]')))
print("waited long enough")

clicks.append(click)
print("clicked clicks")
elements = driver.find_elements_by_class_name('superblock ')
#elements = driver.execute_script('document.getElementsByClassName("map-ui")[0].childElementCount', click)

print("found map-ui")

children = list()
