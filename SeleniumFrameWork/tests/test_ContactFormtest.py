import unittest
import time
import pytest
from SeleniumFrameWork.basepage.BasePage import BaseClass
from SeleniumFrameWork.pages.ContectFormPage import ContactForm
import SeleniumFrameWork.utilities.CustomLogger as cl

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestContactForm(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.cf = ContactForm(self.driver)
        self.bp = BaseClass(self.driver)

    # @pytest.mark.run(order=1)
    def test_formPage(self):
        self.cf.clickContectForm()
        self.cf.verifyFormPage()
        time.sleep(2)
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.clickGender()
        self.cf.enterTech()
        self.cf.enterMessage()
        self.cf.enterCaptha()
        self.cf.clickOnPostButton()


#
# import time
# import pytest
# from SeleniumFrameWork.basepage.BasePage import BaseClass
# from SeleniumFrameWork.pages.ContectFormPage import ContactForm
# import SeleniumFrameWork.utilities.CustomLogger as cl
#
#
# @pytest.mark.usefixtures("beforeClass", "beforeMethod")
# class TestContactForm:
#
#     @pytest.fixture(autouse=True)
#     def classObject(self):
#         self.cf = ContactForm(self.driver)
#         self.bp = BaseClass(self.driver)
#
#     def test_formPage(self):
#         self.cf.clickContectForm()
#         self.cf.verifyFormPage()
#
#     def test_enterData(self):
#         time.sleep(2)
#         self.cf.enterName()
#         self.cf.enterEmail()
#         self.cf.clickGender()
#         self.cf.enterTech()
#         self.cf.enterMessage()
#         self.cf.enterCaptha()
#
#     def test_submitButton(self):
#         self.cf.clickOnPostButton()
