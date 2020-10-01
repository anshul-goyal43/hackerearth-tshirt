from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.hackerearth.com")
login1 = driver.find_element_by_class_name('button__Lyv4')

ActionChains(driver).click(login1).perform()
name = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

name.send_keys("anshul.goyal43@gmail.com",Keys.ENTER)
password.send_keys("bS3eaVUEeM97hYP",Keys.ENTER)

login2 = driver.find_element_by_class_name('submitButton_uHU80')

ActionChains(driver).click(login2).perform()
