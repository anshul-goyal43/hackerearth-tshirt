from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
for i in range(10000000):
    driver.get("https://tezconnect.typeform.com/to/cXgWp2")
    sleep(1)
    s= driver.find_element_by_class_name('button__ButtonWrapper-sc-1g3rldj-0')
    s.click()
    sleep(1)
    na = driver.find_elements_by_class_name('input__InputField-p8yw0p-0')
    na[0].send_keys("some tsjjext", Keys.ENTER)
    sleep(1)
    na[1].send_keys("some tegggsxt", Keys.ENTER)
    sleep(1)
    x = driver.find_element_by_xpath("//input[@placeholder='name@example.com']")
    k = 's'+str(i)+'@gmail.com'
    x.send_keys(k)
    x.send_keys(Keys.CONTROL,Keys.ENTER)
    sleep(1)
