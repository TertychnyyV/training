from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

from selenium import webdriver
driver = webdriver.Chrome('C:/Users/tertychnyy/PycharmProjects/webdriver/chromedriver.exe')
url = driver.get('http://192.168.165.48/OMK/index.html#/login/')
r = requests.get('http://192.168.165.48/OMK/index.html#/login/')

#assert r.status_code == requests.status_codes.ok

def start(driver, url):
    driver.implicitly_wait(1000)
    title = driver.__getattribute__('title')
    try:
        assert 'OMK' in title
        print(f'{title} - test for title PASSED')
    except:
        print('Test for title FAIL')

def test_login_page(driver):
    start(driver, url)
    try:
        driver.find_element(By.XPATH, "//a[@href='mailto:omk-support@cdc.ru']")
        print(f'icon "mail to" has a place')
    except NoSuchWindowException:
        print(f'No icon "mail to"!')
    login(driver)
    driver.implicitly_wait(2000)
    title = driver.__getattribute__('title')
    try:
        assert 'OMK / Авторизация' in title
        print(f'{title} - test for title PASSED')
    except:
        print(f'Test for title FAIL - reason "{title}" not eqal to "OMK1 / Авторизация"')


def login(driver):
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/form/div[1]/div/div/input").send_keys('firm')
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/form/div[2]/div/div/input").send_keys(
        'Administrator')
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/form/div[3]/div/div/input").send_keys('passwd')
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/form/div[4]/button/i/span").click()

start(driver, url)
test_login_page(driver)
login(driver)
driver.close()