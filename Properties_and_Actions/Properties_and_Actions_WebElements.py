import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/seleniumtemplate.html")

myelement = driver.find_element(By.ID,"user_input")

# 1. Check Element Displayed...........
element_Display = myelement.is_displayed()
print("Element is Displayed", element_Display)

# 2. Check Element Enable
element_Enable = myelement.is_enabled()
print("Element is Enable", element_Enable)

# 3. Check Element Size
element_Size = myelement.size
print("Element Size", element_Size)

# 4. Check Element Location
element_Location = myelement.location
print("Element Size", element_Location)

# 5. Click Element
myelement.click()

# 6. Send Text in Element
myelement.send_keys("Sudeep Yadav")
time.sleep(2)

# 7. Clear the text
myelement.clear()
time.sleep(2)

# 8. Send Text in Element
myelement.send_keys("Hello I am Sudeep Yadav")
time.sleep(2)

# 9 Get the text ftom the element
getthetext = myelement.get_attribute("value")
print("Get the text :", getthetext)





time.sleep(5)
driver.quit()