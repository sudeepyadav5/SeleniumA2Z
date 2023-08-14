import time

from SeleniumFrameWork.basepage.DriverClass import WebDriverClass
import SeleniumFrameWork.utilities.CustomLogger as cl
from SeleniumFrameWork.basepage.BasePage import BaseClass
from SeleniumFrameWork.pages.ContectFormPage import ContactForm

wd = WebDriverClass()


driver = wd.getWebDriver("chrome")
bp = BaseClass(driver)
cf = ContactForm(driver)

bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template — DummyPoint")
driver.maximize_window()

cf.clickContectForm()
time.sleep(2)
cf.verifyFormPage()
cf.enterName()
cf.enterEmail()
cf.clickGender()
cf.enterTech()
cf.enterMessage()
cf.enterCaptha()
cf.clickOnPostButton()

time.sleep(5)
driver.minimize_window()
driver.quit()
