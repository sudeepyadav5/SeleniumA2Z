import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/Windows.html")
driver.maximize_window()

wait = WebDriverWait(driver, 25, poll_frequency=25, ignored_exceptions=[NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException])

# To get the current window name
window_Name = driver.current_window_handle
print("Before Switch Window Name is: ", window_Name)
time.sleep(2)

# Click on Popup Button to Open New Window
my_elements = wait.until(lambda x: x.find_elements(By.TAG_NAME, "input"))
for popup in my_elements:
    popupbtn = popup.get_attribute("value")
    print(popupbtn)
    if popupbtn == "Open a Popup Window3":
        popup.click()


# Print the list of Windows are present on the screen session

windows = driver.window_handles
for window in windows:
    print(window)

# Switch the requested of window

driver.switch_to.window(windows[1])
time.sleep(2)

driver.maximize_window()
window_name = driver.current_window_handle
print("After Switch Window Name is: ",window_name)
time.sleep(2)

# Here is the new window performing the action in frame
frame_element = wait.until(lambda x: x.find_element(By.ID, "f4"))

driver.switch_to.frame(frame_element)

framedata = wait.until(lambda x: x.find_element(By.ID, "framename"))
print(" Frame Name is: ", framedata.text)

time.sleep(5)
driver.quit()