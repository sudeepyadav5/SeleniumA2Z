import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://dummypoint.com/seleniumtemplate.html")

# Find By ID
# driver.find_element(By.ID, "user_input").send_keys("Sudee By ID")

# Find By Name
# driver.find_element(By.NAME, "textbox").send_keys("Sudeep By Name")

# Find By ClassName
# driver.find_element(By.CLASS_NAME, "entertext").send_keys("Sudeep By ClassName")

# Find By TagName
# driver.find_element(By.TAG_NAME, "input").send_keys("Sudeep By Tag Name")

# Find By Link Text
# driver.find_element(By.LINK_TEXT, "Frame").click()

# Find Partial Link Text
driver.find_element(By.PARTIAL_LINK_TEXT, "Win").click()




time.sleep(5)
driver.quit()