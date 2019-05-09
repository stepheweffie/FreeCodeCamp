from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
# Build webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless')
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
driver.close()


def shorten_path(line):
    if 'Introduction' in line:
        line = line.replace('Introduction', 'Intro')
    if 'Javascript' in line or 'JavaScript' in line:
        line = line.replace('Javascript', 'JS')
        line = line.replace('JavaScript', 'JS')
    if 'Regular Expressions' in line:
        line = line.replace('Regular Expressions', 'RegEx')
    if 'Algorithms' in line:
        line = line.replace('Algorithms', 'Algos')
    if 'Certification' in line:
        line = line.replace('Certification', 'Cert')
    line = line.rstrip()
    return line


def iterate_files(line):
    '''
    :param line:
    :param parent_dir:
    :return: Files with different endings within the current directory
    '''
    try:
        shorten_path(line)
        pwd = os.getcwd()
        #print('Inside ' + pwd + ' and ' + parent_dir + ' working on ' + line)
        if 'Responsive' in pwd or 'Bootstrap' in pwd:
            ex_file = open(line + '.html', 'w', encoding='UTF-8')
        elif 'Mongoose' or 'Chai' or 'Helment' or 'Express' or 'npm' in pwd:
            ex_file = open(line + '.txt' 'w', encoding='UTF-8')
        elif 'Sass' in pwd:
            ex_file = open(line + '.css', 'w', encoding='UTF-8')
        else:
            ex_file = open(line + '.js', 'w', encoding='UTF-8')
        ex_file.close()
    except FileNotFoundError:
        try:
            line = line[:len(line)//2]
            ex_file = open(line + '.js', 'w', encoding='UTF-8')
            ex_file.close()
        except FileNotFoundError:
            print('File Not Found Error')
            pass
    except OSError:
        line = 'Invalid_Chars'
        ex_file = open(line + '.js', 'w', encoding='UTF-8')
        ex_file.close()


def fcc_curriculum():
    '''
    :return: Makes directories and calls iterate_fies to create files
    '''

    read_file = open('tree.txt', 'r', encoding='UTF-8')
    read_lines = read_file.readlines()
    print('Building curriculum')
    data = list()
    for d in read_lines:
        data.append(d)
        #print(d)
    print(len(data))
    read_file.close()
    switch = 0
    count = 0
    try:
        for dirs in data:
            count += 1
            # Omit \n from dir name
            l = str(dirs[:-1])
            print(l)
            pwd = os.getcwd()
            print(pwd)
            if '300' in l and count > 1:
                os.chdir('..')
                os.chdir('..')
                os.chdir('..')
            if 'Not Passed' not in l:
                if '300' not in l:
                    switch += 1
                    if 'Introduction' in l:
                        switch = 2
                    elif 'Problem' in l:
                        switch = 1
                else:
                    switch = 0
                # Prints following statement, but does not mkdir, does not throw error
                if switch > 2:
                    os.chdir('..')
                    os.chdir('..')
                    switch = 1
                #print('Making directory')
                #pwd = os.getcwd()
                if 'Interview Prep' in l:
                    os.chdir('..')
                    switch = 1
                l = shorten_path(l)
                #if '\\\\?\\' not in pwd:
                #    npwd = '\\\\?\\' + pwd + '\\' + l
                #else:
                npwd = os.getcwd() + '\\' + l
                print(npwd)
                os.mkdir(npwd)
                print('Directory made')
                os.chdir(npwd)
                print('Inside new directory')
            else:
                if l == 'Not Passed\n':
                    pass
                else:
                    l = l[10:]
                if '*' in l:
                    l.replace('*', '')
                iterate_files(l)
    except FileExistsError:
        pass


if __name__ == '__main__':
    print('Preparing to build tree ')
    fcc_curriculum()