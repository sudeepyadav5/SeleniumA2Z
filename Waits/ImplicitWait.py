import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://dummypoint.com/seleniumtemplate.html")

driver.implicitly_wait(10)

driver.find_element(By.ID, "user_input").send_keys("Sudee By ID")

time.sleep(5)
driver.quit()