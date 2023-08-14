from traceback import print_stack

from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
import allure
import SeleniumFrameWork.utilities.CustomLogger as cl


class BaseClass:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def launchWebPage(self, url, title):
        try:
            self.driver.get(url)
            assert title in self.driver.title
            self.log.info("Web Page Launch with " + url)
        except:
            self.log.info("Web Page Not Launch with " + url)

    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error(f"Locator Type {locatorType} entered not found")
            print_stack()

        return False

    def getWebElement(self, locatorValue, locatorType="id"):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            webElement = self.driver.find_element(locatorByType, locatorValue)
            self.log.info(f"Web Element found with locator value {locatorValue} using locator type {locatorByType}")
        except:
            self.log.error(
                f"Web Element Not found with locator value {locatorValue} using locator type {locatorByType}")
            print_stack()

        return webElement

    def waitForElement(self, locatorValue, locatorType="id"):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            # webElement = self.driver.find_element(locatorByType, locatorValue)
            webElement = wait.until(lambda x: x.find_element(locatorByType, locatorValue))
            self.log.info(f"Web Element found with locator value {locatorValue} using locator type {locatorByType}")
        except:
            self.log.error(
                f"Web Element Not found with locator value {locatorValue} using locator type {locatorByType}")
            print_stack()
            self.takeScreenshot(locatorType)
            assert False
        return webElement

    def clickOnElement(self, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.click()
            self.log.info(f"Click On Web Element with locator value {locatorValue} using locator type {locatorType}")
        except:
            self.log.error(
                f"Unable to Click On Element with locator value {locatorValue} using locator type {locatorType}")
            print_stack()
            assert False

    def sendText(self, text, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.send_keys(text)
            self.log.info(
                f"Send the text {text} in Web Element with locator value {locatorValue} using locator type {locatorType}")
        except:
            self.log.info(
                f"Unable to Send the text {text} in Web Element with locator value {locatorValue} using locator type {locatorType}")
            print_stack()
            self.takeScreenshot(locatorType)
            assert False

    def getText(self, locatorValue, locatorType="id"):
        elementText = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            elementText = webElement.text
            self.log.info(
                f"Got the text {elementText} in Web Element with locator value {locatorValue} using locator type {locatorType}")
        except:
            self.log.info(
                f"Unable to get the text {elementText} in Web Element with locator value {locatorValue} using locator type {locatorType}")
            print_stack()

        return elementText

    def isElementDisplayed(self, locatorValue, locatorType="id"):
        elementDisplayed = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            elementDisplayed = webElement.is_displayed()
            self.log.info(
                f" Web Element is Displayed web page with locator value {locatorValue} using locator type {locatorType}")
        except:
            self.log.info(
                f" Web Element is Not Displayed web page with locator value {locatorValue} using locator type {locatorType}")
            print_stack()

        return elementDisplayed

    def scrollTo(self, locatorValue, locatorType="id"):
        actions = ActionChains(self.driver)
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            actions.move_to_element(webElement).perform()
            self.log.info(
                f"Scrolled to WebElement with locator value {locatorValue} using locator type {locatorType}")
        except:
            self.log.info(
                f"Unable to Scroll to WebElement with locator value {locatorValue} using locator type {locatorType}")
            print_stack()

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)
