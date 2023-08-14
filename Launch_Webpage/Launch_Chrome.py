import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://dummypoint.com/")

time.sleep(5)
driver.quit()
