import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome()
driver.get("http://dummypoint.com/seleniumtemplate.html")

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException])



# ele = wait.until(lambda x: x.find_element(By.ID, "user_input"))
ele = wait.until(ec.presence_of_element_located((By.ID, "user_input")))
ele.send_keys("Sudee By ID")



time.sleep(5)
driver.quit()