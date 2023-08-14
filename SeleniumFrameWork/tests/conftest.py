import time
import pytest
from SeleniumFrameWork.basepage.BasePage import BaseClass
from SeleniumFrameWork.basepage.DriverClass import WebDriverClass


# @pytest.yield_fixture(scope='class')
@pytest.fixture(scope='class')
def beforeClass(request):
    print("Before Class")
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver("chrome")
    bp = BaseClass(driver)
    bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template — DummyPoint")
    driver.maximize_window()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.minimize_window()
    driver.quit()
    print("After the class")


# @pytest.yield_fixture()
@pytest.fixture()
def beforeMethod():
    print("Before Method")
    yield
    print("After Method")
