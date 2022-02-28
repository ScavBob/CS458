from random import randint

from selenium import webdriver
import os
import time

from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)


# TEST CASE 1 #
def testcase1():
    mails = ['walther.evans@yahoo.com', '']

    for i in range(10):
        driver.get('http://localhost:8000/')
        driver.find_element_by_id('email_and_phone').send_keys(mails[i])
        assert True == True
    return None


def runTestCases():
    testcase1()


runTestCases()
