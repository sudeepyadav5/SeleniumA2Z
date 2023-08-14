import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://dummypoint.com/seleniumtemplate.html")

# Below are some ways to find WebElement using CssSelector

# 1. To write id name in css selector you need to add "#" before id value
# driver.find_element(By.CSS_SELECTOR, "#user_input").send_keys("Sudeep By CSS ID")

# 2. To write class name in css selector you need to add "." before class name
# driver.find_element(By.CSS_SELECTOR, ".entertext").send_keys("Sudeep By CSS Class")

# 3. Using " Tag name("input") and name " Attribute value as css_selector
# driver.find_element(By.CSS_SELECTOR, "input[name='textbox']").send_keys("sudeep by tag with name attribute")

# 4. Using " Tag name("input"),className and name " Attribute value as css_selector
# driver.find_element(By.CSS_SELECTOR, "input[class='entertext']").send_keys("sudeep by tag with name attribute")
# driver.find_element(By.CSS_SELECTOR, "input.entertext[name='textbox']").send_keys("sudeep by tag with name attribute")

# 5. “^” - Find elements using starts with a string value
# driver.find_element(By.CSS_SELECTOR, "input[name^='te']").send_keys("sudeep by tag with name attribute")

# 6. “$” - Find elements using Ends with a string value
driver.find_element(By.CSS_SELECTOR, "input[name$='ox']").send_keys("sudeep by tag with name attribute")

# 7. “*” - Find elements using contains a substring.
driver.find_element(By.CSS_SELECTOR, "input[name*='xtb']").send_keys("sudeep by tag with name attribute")



time.sleep(5)
driver.quit()