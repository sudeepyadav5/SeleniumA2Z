import time
import pytest
from SeleniumFrameWork.basepage.BasePage import BaseClass
from SeleniumFrameWork.pages.EnterTextPage import EnterText
import SeleniumFrameWork.utilities.CustomLogger as cl
import unittest


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestEnterText(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.et = EnterText(self.driver)

    def test_clickOnTextPage(self):
        self.et.clickOnLocatorPage()
        time.sleep(2)
        self.et.enterText()
        self.et.clickOnSubmitButton()
