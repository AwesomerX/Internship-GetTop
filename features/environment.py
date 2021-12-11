from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from app.application import Application
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



def browser_init(context):


#    service = Service('C:/Users/Chopp/Automation/Internship-GetTop/chromedriver.exe')
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.app = Application(context.driver)
    action = ActionChains()


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


