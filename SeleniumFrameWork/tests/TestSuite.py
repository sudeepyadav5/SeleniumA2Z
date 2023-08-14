"""# 1.Import the files

import unittest
from SeleniumFrameWork.tests.test_ContactFormtest import TestContactForm
from SeleniumFrameWork.tests.test_EnterTextTest import TestEnterText

# 2.Create the Object of the class using unittest
cf = unittest.TestLoader().loadTestsFromTestCase(TestContactForm)
et = unittest.TestLoader().loadTestsFromTestCase(TestEnterText)

# 3.Create TestSuite
regressionTest = unittest.TestSuite([cf,et])

# 4.Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)
"""

import unittest
from SeleniumFrameWork.tests.test_ContactFormtest import TestContactForm
from SeleniumFrameWork.tests.test_EnterTextTest import TestEnterText

# Create the Object of the class using unittest
cf = unittest.TestLoader().loadTestsFromTestCase(TestContactForm)
et = unittest.TestLoader().loadTestsFromTestCase(TestEnterText)

# Create TestSuite
regressionTest = unittest.TestSuite([cf, et])

# Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)
