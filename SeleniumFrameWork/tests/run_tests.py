import subprocess
import unittest

number_of_runs = 2
for _ in range(number_of_runs):
    subprocess.run(["pytest", "-k", "test_EnterTextTest.py"])

# Generate Allure report
subprocess.run(["allure", "generate", "allure-results"])

"""if __name__ == '__main__':
    # Loop three times to run the test suite
    for _ in range(3):
        unittest.main()
"""

