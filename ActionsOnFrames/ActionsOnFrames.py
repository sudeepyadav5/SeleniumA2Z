import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/Frame.html")

myiframe = driver.find_elements(By.TAG_NAME, "iframe")

# Display Number of iframe n this webpage
print(len(myiframe))

"""# Switch to iframe by index
time.sleep(2)
driver.switch_to.frame(1)
"""

"""# Switch to iframe by Name
time.sleep(2)
driver.switch_to.frame("farme4")
"""

# Switch to iframe by id
time.sleep(2)
driver.switch_to.frame("f3")

currentframename = driver.find_element(By.ID, "framename")
print("Frame Name is : ", currentframename.text)

# Switch back to normal content page from frame

time.sleep(2)
driver.switch_to.default_content()

currentframename = driver.find_element(By.ID, "framename")
print("Web Page is : ", currentframename.text)

time.sleep(5)
driver.quit()
