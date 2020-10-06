from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("https://tezconnect.typeform.com/to/cXgWp2")
sleep(3)
s= driver.find_element_by_class_name('button__ButtonWrapper-sc-1g3rldj-0')
s.click()
sleep(3)
na = driver.find_elements_by_class_name('input__InputField-p8yw0p-0')
na[0].send_keys("some tsjjext",Keys.ENTER)
sleep(2)
na[1].send_keys("some tegggsxt",Keys.ENTER)
sleep(3)
x = driver.find_element_by_xpath("//input[@placeholder='name@example.com']")
#print(x)
x.send_keys("shhhhasmes@gmail.com")
x.send_keys(Keys.CONTROL,Keys.ENTER)
