import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/Frame.html")
driver.maximize_window()


wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException])

myelement = wait.until(lambda x: x.find_element(By.LINK_TEXT, "Form"))

# 1. Create the object of ActionChains
actions = ActionChains(driver)

# 2. Double Click
actions.double_click(myelement).perform()


"""# 3. Right Click
# actions.context_click().perform()
actions.context_click(myelement).perform()"""

time.sleep(5)
driver.quit()