from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestPageContent(unittest.TestCase):

    def setUp(self):
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Firefox(options=firefox_options)

    def test_page_elements(self):
        driver = self.driver
        driver.get("http://10.48.229.180")

        wait = WebDriverWait(driver, 10)

        h1 = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertEqual("Lab 5-1 COMPLETE!", h1.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

