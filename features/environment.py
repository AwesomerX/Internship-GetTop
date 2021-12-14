from selenium.webdriver.chrome.service import Service
from app.application import Application
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def browser_init(context):

#    service = Service('C:/Users/Chopp/Automation/Internship-GetTop/chromedriver.exe')

    #context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver = webdriver.Firefox(executable_path='C:/Users/Chopp/Automation/Internship-GetTop/geckodriver.exe')
    context.driver.maximize_window()
    context.app = Application(context.driver)


    ###  HEADLESS MODE  ###

    #chrome_options = Options()
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument('--no-sandbox')
    #driver = webdriver.Chrome('C:/Users/Chopp/Automation/Internship-GetTop/chromedriver.exe', options=chrome_options)
    #driver.get('http://www.gettop.us')
    #context.app = Application(context.driver)
    #print('test')
    #driver.close()

    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #driver = webdriver.Chrome('C:/Users/Chopp/Automation/Internship-GetTop/chromedriver.exe', chrome_options=options)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


