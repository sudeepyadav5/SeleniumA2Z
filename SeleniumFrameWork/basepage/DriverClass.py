from selenium import webdriver
import SeleniumFrameWork.utilities.CustomLogger as cl

class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            driver = webdriver.Chrome()
            self.log.info("Chrome Driver is Initialising")

        elif browserName == "firefox":
            driver = webdriver.Firefox()
            self.log.info("Firefox Driver is Initialising")

        elif browserName == "safari":
            driver = webdriver.Safari()
            self.log.info("Safari Driver is Initialising")

        return driver
