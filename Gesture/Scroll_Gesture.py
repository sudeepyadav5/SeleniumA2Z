from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import time



driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/Form.html")
assert "Selenium Template — DummyPoint" in driver.title, "Error Title is incorrect as expected title......"
driver.maximize_window()
wait = WebDriverWait(driver, 15, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
wait.until(lambda x: x.find_element(By.ID, "reused_form"))

name = wait.until(lambda x: x.find_element(By.ID, "name"))
name.send_keys("Sudeep Yadav")

email = wait.until(lambda x: x.find_element(By.ID, "email"))
email.send_keys("sudeep@appscrip.com")

genders = wait.until(lambda x: x.find_elements(By.XPATH, "//div/input[@name='gender']"))
for gender in genders:
    genderlabel = gender.get_attribute('value')
    print(genderlabel)
    if genderlabel == "male":
        gender.click()
technology = wait.until(lambda x: x.find_element(By.ID, "tech"))
technology.send_keys("SDET")

"""# 1. Scroll the page and find element
message = wait.until(lambda x: x.find_element(By.ID, "message"))
actions = ActionChains(driver)
actions.move_to_element(message).perform()
"""

"""# 2.  Scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
message = wait.until(lambda x: x.find_element(By.ID, "message"))"""


"""# 3. Scroll up the page
driver.execute_script("window.scrollTo(0, 0);")
message = wait.until(lambda x: x.find_element(By.ID, "message"))
"""
# 4. Scroll to a specific element
message = wait.until(lambda x: x.find_element(By.ID, "message"))
driver.execute_script("arguments[0].scrollIntoView();", message)

message.send_keys("Hello I am Sudeep Yadav and I am Good QA")

getcaptcha = wait.until(lambda x: x.find_element(By.ID, "captcha_image"))

send_captcha = wait.until(lambda x: x.find_element(By.ID, "captcha"))
send_captcha.send_keys(getcaptcha.text)

time.sleep(2)

postbtn = wait.until(lambda x: x.find_element(By.ID, "btnContactUs"))

postbtn.click()


time.sleep(5)
driver.minimize_window()
driver.quit()