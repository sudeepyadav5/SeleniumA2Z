from SeleniumFrameWork.basepage.BasePage import BaseClass
import SeleniumFrameWork.utilities.CustomLogger as cl

class EnterText(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Locator Form
    _locatorpage = "Locators" #link
    _enterTextEditBox = "user_input" # id
    _clickSubmitButton = "submitbutton" # id

    def clickOnLocatorPage(self):
        self.clickOnElement(self._locatorpage, "link")

    def enterText(self):
        self.sendText("Sudeep Yadav", self._enterTextEditBox, "id")

    def clickOnSubmitButton(self):
        self.clickOnElement(self._clickSubmitButton, "id")
