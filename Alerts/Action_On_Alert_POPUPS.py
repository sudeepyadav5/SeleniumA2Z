
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
# Import Alert class
from selenium.webdriver.common.alert import Alert
driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/Windows.html")
driver.maximize_window()

wait = WebDriverWait(driver, 25, poll_frequency=25, ignored_exceptions=[NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException])

promtalertbtn = wait.until(lambda x: x.find_element(By.NAME, "promtalertb"))
promtalertbtn.click()

# Create the object for the Alert class
alert_btn = Alert(driver)
time.sleep(2)

# Using object class call the method to "1. Accept , 2. dismiss and 3. send text and get text" in the alert text
# alert_btn_Text = alert_btn.text
# print(alert_btn_Text)
#

alert_btn.send_keys("Sudeep Yadav")
# alert_btn.accept()
alert_btn.dismiss()

time.sleep(5)
driver.quit()