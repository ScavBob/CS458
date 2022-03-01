from random import randint

from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)


# TEST CASE 1 #
# TEST WRONG CREDENTIALS
def testcase1():
    mails = ['walther.evans@yahoo.com', 'derek.johnson@mail.com', 'cankatkadim@gmail.com', '+905442316335']
    passwords = ['thispassisnotcommon', 'thispassisnotcommon', 'clearlyawrongpass', 'clearlyanotherwrongpass']
    for i in range(len(mails)):
        driver.get('http://localhost:8000/')
        driver.find_element_by_id('email_and_phone').send_keys(mails[i])
        driver.find_element_by_id('password').send_keys(passwords[i])
        driver.find_element_by_xpath('//*[@id="login_form"]/div[3]/button').click()
        title = driver.title
        assert title == 'Netflix Login', 'Unexpected Process Results'
        print('Process Failed Successfully')


# TEST EMPTY CREDENTIALS
def testcase2():
    mails = ['', 'derek.johnson@mail.com', '']
    passwords = ['thispassisnotcommon', '', '']
    for i in range(len(mails)):
        driver.get('http://localhost:8000/')
        driver.find_element_by_id('email_and_phone').send_keys(mails[i])
        driver.find_element_by_id('password').send_keys(passwords[i])
        driver.find_element_by_xpath('//*[@id="login_form"]/div[3]/button').click()
        title = driver.title
        assert title == 'Netflix Login', 'Unexpected Process Results'
        print('Process Failed Successfully')


# TEST LENGTH RESTRICTIONS
def testcase3():
    mails = ['cankatkadim@gmail.com', 'cankatkadim@gmail.com']
    passwords = ['sho', 'abittoolongtobearealpasswordthisoneamirightoriamrightofcourseamright']
    for i in range(len(mails)):
        driver.get('http://localhost:8000/')
        driver.find_element_by_id('email_and_phone').send_keys(mails[i])
        driver.find_element_by_id('password').send_keys(passwords[i])
        driver.find_element_by_xpath('//*[@id="login_form"]/div[3]/button').click()
        title = driver.title
        assert title == 'Netflix Login', 'Unexpected Process Results'
        print('Process Failed Successfully')


# TEST FACEBOOK LOGIN
def testcase4():
    driver.get('http://localhost:8000/')
    driver.find_element_by_xpath('//*[@id="login_form"]/div[5]/a').click()
    title = driver.title
    assert title == 'Netflix Login', 'Unexpected Process Results'
    print('Process Failed Successfully')


# TEST PASSWORD COPY/PASTE
def testcase5():
    driver.get('http://localhost:8000/')
    action = ActionChains(driver)
    driver.find_element_by_id('email_and_phone').send_keys('asdfasd061@gmail.com')
    driver.find_element_by_id('password').send_keys('thispassisnotcommon')
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    driver.find_element_by_id('password').send_keys('thispasswillfail')
    action.key_down(Keys.CONTROL).send_keys('a').send_keys('v').key_up(Keys.CONTROL).perform()
    driver.find_element_by_xpath('//*[@id="login_form"]/div[3]/button').click()
    title = driver.title
    assert title == 'Netflix Login', 'Unexpected Process Results'
    print('Process Failed Successfully')


# TEST CROSS-SITE SCRIPTING AND SQL INJECTIONS
def testcase6():
    mails = ["test@test.test' or 1=1; drop table user;--", "XSStest@xss"]
    passwords = ['test', '<script>alert()</script>']
    driver.get('http://localhost:8000/')
    for i in range(len(mails)):
        driver.find_element_by_id('email_and_phone').send_keys(mails[i])
        driver.find_element_by_id('password').send_keys(passwords[i])
        driver.find_element_by_xpath('//*[@id="login_form"]/div[3]/button').click()
        title = driver.title
        assert title == 'Netflix Login', 'Unexpected Process Results'
        print('Process Failed Successfully')


def runTestCases():
    testcase1()
    testcase2()
    testcase3()
    testcase4()
    testcase5()
    testcase6()
    driver.close()


runTestCases()
