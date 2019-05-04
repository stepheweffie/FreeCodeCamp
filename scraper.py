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


#svg = driver.find_elements_by_xpath('//*[@id="___gatsby"]/div/main/div/div[4]/ul/li[1]/div/svg')
#svg.click()
#svg1 = driver.find_elements_by_xpath('//*[@id="___gatsby"]/div/main/div/div[4]/ul/li[1]/ul/li[1]/div/svg')
#svg1.click()
# Cannot click svgs

#try:
#    li = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'superblock open')))
#except TimeoutException:
#    wait = wait

#close_list = driver.find_element_by_xpath('//*[@class="superblock open"]/div')
#close_list.click()
#close_list1 = driver.find_element_by_xpath('//*[@class="block open"]/div')
#close_list1.click()
modules = driver.find_elements_by_class_name('superblock ')
#li = driver.find_element_by_class_name('superblock open') InvalidSelectorException
#li = driver.find_element_by_class_name('block open') Invalid SelectorExeption

children = list()
for module in modules:
    print(module.text)
    children.append(module.text)

