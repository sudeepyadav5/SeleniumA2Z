from SeleniumFrameWork.basepage.BasePage import BaseClass
import SeleniumFrameWork.utilities.CustomLogger as cl

class ContactForm(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator Value in Contact form page

    _contactFormPage = "Form" # link
    _formPage = "reused_form" # id
    _enterName = "name" # id
    _enterEmail = "email" # id
    _gender = "//input[@value='male']" # xpath
    _enterTech = "tech" # id
    _enterMessage = "message" # id
    _getcaptcha = "captcha_image" # id
    _enterCaptcha = "captcha" # id
    _postButton = "//button[@id='btnContactUs']" # xpath


    def clickContectForm(self):
        self.clickOnElement(self._contactFormPage, "link")
        cl.allureLogs("Click On Contact Form")

    def verifyFormPage(self):
        element = self.isElementDisplayed(self._formPage, "id")
        assert element == True
        cl.allureLogs("Verified the Contact Form")

    def enterName(self):
        self.sendText("Sudeep", self._enterName, "id")
        cl.allureLogs("Entered Name")

    def enterEmail(self):
        self.sendText("Sudeep@appscrip.co", self._enterEmail, "id")
        cl.allureLogs("Entered Email")

    def clickGender(self):
        self.clickOnElement(self._gender, "xpath")
        cl.allureLogs("Selected Gender")

    def enterTech(self):
        self.sendText("SDET", self._enterTech, "id")
        cl.allureLogs("Entered Technology")

    def enterMessage(self):
        self.sendText("Hello I am Sudeep, and SDET", self._enterMessage, "id")
        cl.allureLogs("Entered Message")

    def getCaptha(self):
        cap = self.getText(self._getcaptcha, "id")
        cl.allureLogs("Got the Captcha")
        return cap

    def enterCaptha(self):
        self.sendText(self.getCaptha(), self._enterCaptcha, "id")
        cl.allureLogs("Entered Captcha")

    def clickOnPostButton(self):
        self.scrollTo(self._postButton, "xpath")
        cl.allureLogs("Scrolled the Page")
        self.clickOnElement(self._postButton, "xpath")
        cl.allureLogs("Clicked the Post Button")





