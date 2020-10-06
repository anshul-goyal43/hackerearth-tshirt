from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.get("https://tezconnect.typeform.com/to/cXgWp2")
sleep(10)
s= driver.find_element_by_class_name('button__ButtonWrapper-sc-1g3rldj-0')
s.click()
sleep(10)
name = driver.find_elements_by_class_name('spacer__Spacer-sc-11bdvt0-0')
sleep(10)
