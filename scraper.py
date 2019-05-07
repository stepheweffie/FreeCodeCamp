from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
# Build webdriver
options = webdriver.ChromeOptions()
options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://learn.freecodecamp.org/')
wait = WebDriverWait(driver, 15)


def write_element_text(elements):
    '''
    :param elements: For each open superblock class element
    :return: Writes lines of each elements
    '''
    file.writelines(elements.text)
    #children.append(element.text)
    file.write('\n')

# Open a text file to write


file = open('tree.txt', 'w', encoding='UTF-8')


# Scrape the modules for dirs and file names
parents = driver.find_elements_by_class_name('superblock ')
for element in parents:
    element.click()
child_nodes = driver.find_elements_by_class_name('block ')
for element in child_nodes:
    element.click()
# This is counter intuitive because the open div has a class name 'superblock open', there are no 'superblock ' divs
grandchild_nodes = driver.find_elements_by_class_name('superblock ')
for element in grandchild_nodes:
    write_element_text(element)

file.close()


def iterate_files(line, parent_dir):
    '''

    :param line:
    :param parent_dir:
    :return: Files with different endings within the current directory
    '''
    pwd = os.getcwd()
    print('Inside ' + pwd + ' and ' + parent_dir + ' working on ' + line)
    if line != "Not Passed\n":
        line = line[10:]
        if 'Responsive' or 'Data' in parent_dir or 'Bootstrap' in pwd:
            ex_file = open(line + '.html', 'w', encoding='UTF-8')
        elif 'Projects' or 'Mongoose' or 'Chai' or 'Helment' or 'Express' or 'npm' in pwd:
            ex_file = open(line + '.txt' 'w', encoding='UTF-8')
        elif 'Sass' in pwd:
            ex_file = open(line + '.css', 'w', encoding='UTF-8')
        else:
            ex_file = open(line + '.js', 'w', encoding='UTF-8')
        ex_file.close()


def fcc_curriculum():
    '''
    :return: Makes directories and calls iterate_fies to create files
    '''

    read_file = open('tree.txt', 'r', encoding='UTF-8')
    read_lines = read_file.readlines()
    print('Building curriculum')
    try:
        for dirs in read_lines:
            # Omit \n from dir name
            l = dirs[:-1]
            pwd = os.getcwd()
            parent = str()
            if '300' in pwd:
                parent = pwd
            if 'Project' in pwd and '300' in l:
                os.chdir('..')
                os.chdir('..')
                os.chdir('..')
            if 'Not Passed' not in l:
                # Prints following statement, but does not mkdir, does not throw error
                print('Making directory')
                os.mkdir(l)
                os.chdir(l)
                print('Inside new directory')
            else:
                print('Creating file' + l)
                iterate_files(l, parent)

    except FileExistsError:
        pass
    read_file.close()


#if __name__ == '__main__':
print('Preparing to build tree ')
fcc_curriculum()