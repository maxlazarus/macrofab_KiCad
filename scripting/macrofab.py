'''
@author: Max Prokopenko
@email : max@embeddedprofessional.com
@github: https://github.com/maxlazarus
'''
from __future__ import print_function
from __future__ import unicode_literals
import os
from os import path
from os import sep

import codecs

'''
web-related constants
'''
top_level_domain = r'https://factory.macrofab.com'
image_folder_path = sep + r'browser_images'
parts_path = r'/parts'

root = os.path.split(os.path.abspath(__file__))[0]

def clear_images():
    '''
    clears all the files in the image_folder_path location
    '''
    folder = root + sep + image_folder_path
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            os.unlink(file_path)
        except Exception, e:
            print(e)

def install_dependencies():
    '''
    install Selenium webdriver
    '''
    import platform
    from subprocess import call
    if platform.system() == 'Windows':
        call (['python', '-m', 'pip', 'install', '-U', 'selenium']) #WINDOWS
    else:
        call (['sudo', 'pip', 'install', '-U', 'selenium']) #LINUX, OSX
    from selenium import webdriver, common  # @NoMove @Reimport @UnusedImport

try:
    from selenium import webdriver, common  # @NoMove @UnusedImport
except:
    try:
        install_dependencies()
    except:
        execfile('get-pip.py')
        install_dependencies()

def disconnect(browser):
    print('Disconnecting')
    browser.close()
    browser.quit()

def get_browser():
    '''clears images and returns a new PhantomJS Selenium webdriver object'''
    try:
        browser = webdriver.PhantomJS()
    except:
        browser = webdriver.PhantomJS('./phantomjs')
    browser.implicitly_wait(3)
    browser.delete_all_cookies()
    clear_images()
    print('Browser opened')
    return browser

'''
//*[@id="partRow0"]/td[3]
//*[@id="partRow1"]/td[3]
//*[@id="partRow0"]/td[1]/a
'''
'''
    filename = 'test.html'
    f = codecs.open(filename, 'w', 'utf-8')
    for line in content:      
        f.write(line)
    f.close()
'''
row0_xpath = '//*[@id="partRow0"]/td[3]'

if __name__ == '__main__':
    print('by Max Prokopenko max@embeddedprofessional.com')
    b = get_browser()
    b.get(top_level_domain + parts_path)

    with codecs.open('test.txt', 'w', 'utf-8') as f:
        for line in b.page_source: f.write('file')

    print(b.find_element_by_xpath(row0_xpath))
    b.save_screenshot(image_folder_path + sep + 'first_try.png')
    disconnect(b)
