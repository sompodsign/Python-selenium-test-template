import pathlib  # Added This line to skip error
import sys
import os.path
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from testconf.testData_configuration_for_run_test import *
from utils import ExcelUtils
from webdriver_manager.chrome import ChromeDriverManager

# from builtins import set
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class BaseTest(unittest.TestCase):
    clientPath = pathlib.Path(__file__).parent / f"../TestData/{File_Name_of_the_instance}"

    def setUp(self):
        options = Options()
        # options.add_argument("--start-fullscreen")
        # options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        # self.driver = webdriver.Chrome(executable_path=pathlib.Path(__file__).parent / "../browser/chromedriver.exe", options=options)

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(300)
        # print(ExcelUtils.readData(self.clientPath, 'LoginData', 2, 3))
        self.driver.get(ExcelUtils.readData(self.clientPath, 'LoginData', 2, 3))

    def tearDown(self):
        self.driver.close()


# class TestCase(object):
#     pass
#
#
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
#     unittest.TextTestRunner(verbosity=1).run(suite)
