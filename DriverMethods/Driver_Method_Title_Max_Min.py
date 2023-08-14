import time

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/")
assert "General Dashboard — DummyPoint" in driver.title, "Title is Not Correct with Expected Title"
driver.maximize_window()
time.sleep(5)
driver.minimize_window()

time.sleep(2)
driver.quit()