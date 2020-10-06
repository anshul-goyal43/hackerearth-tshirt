from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.get("https://tezconnect.typeform.com/to/cXgWp2")
sleep(9)
s= driver.find_element_by_class_name('button__ButtonWrapper-sc-1g3rldj-0')
s.click()
sleep(9)
#name = driver.find_elements_by_class_name('spacer__Spacer-sc-11bdvt0-0')
#name[0].click()
na = driver.find_elements_by_class_name('input__InputField-p8yw0p-0')
na[0].send_keys("some text",Keys.ENTER)
sleep(9)
#aa = driver.find_elements_by_class_name('input__InputField-p8yw0p-0')
na[1].send_keys("some text",Keys.ENTER)
sleep(8)
x = driver.find_element_by_xpath("//input[@placeholder='name@example.com']")
x.send_keys("some@gmail.com",Keys.ENTER)
