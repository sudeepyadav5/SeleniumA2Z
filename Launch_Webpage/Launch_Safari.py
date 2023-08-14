import time

from selenium import webdriver

driver = webdriver.Safari()
driver.get("http://dummypoint.com/")

time.sleep(5)
driver.quit()

