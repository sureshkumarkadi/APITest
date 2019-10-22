from selenium import webdriver

import time

browser = webdriver.Chrome('D:\Demoproject\Env\chromedriver.exe')

browser.get('http://automationpractice.com')

time.sleep(1)

Login_button=browser.find_element_by_xpath("//a[@class='login']")

Login_button.click()

time.sleep(1)

enter_email = browser.find_element_by_xpath("//input[@name='email_create']")

enter_email.send_keys("suresh4978@gmail.com")

time.sleep(1)

submit = browser.find_element_by_xpath("//button[@id='SubmitCreate']")

submit.click()
time.sleep(5)
browser.close()