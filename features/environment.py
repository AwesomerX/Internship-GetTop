from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


service = Service('C:/Users/Chopp/Automation/Internship-GetTop/chromedriver.exe')

driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://www.gettop.us')

action = ActionChains(driver)
#firstlevelmenu = driver.find_element(By.ID, 'ul.header-nav.header-nav-main.nav.nav-left.nav-uppercase')
#action.move_to_element(firstlevelmenu).perform()
#secondlevelmenu = driver.find_element( put element here)
#secondlevelmenu.click()
'''
# find the element to use here
parent_level_menu = driver.find_element()
action.move_to_element(parent_level_menu).perform()

# find the element to use here
child_level_menu = driver.find_element()
child_level_menu.click()
'''
sleep(5)

driver.close()

