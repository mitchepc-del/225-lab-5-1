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

```
def test_page_elements(self):
    driver = self.driver
    driver.get("http://10.48.229.180")

    wait = WebDriverWait(driver, 10)

    # Check H1 title
    h1 = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    self.assertEqual("Lab 5-1 COMPLETE!", h1.text)

    # Check H2 section title
    h2 = driver.find_element(By.TAG_NAME, "h2")
    self.assertEqual("Congratulations!", h2.text)

    # Check subtitle paragraph
    subtitle = driver.find_element(By.CLASS_NAME, "subtitle")
    self.assertIn("CIT 225", subtitle.text)

    # Check button exists
    button = driver.find_element(By.TAG_NAME, "button")
    self.assertTrue(button.is_displayed())

def test_button_interaction(self):
    driver = self.driver
    driver.get("http://10.48.229.180")

    wait = WebDriverWait(driver, 10)

    # Click the button
    button = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
    button.click()

    # Verify message appears
    message = wait.until(EC.presence_of_element_located((By.ID, "message")))
    self.assertNotEqual("", message.text)

def tearDown(self):
    self.driver.quit()
```

if **name** == "**main**":
unittest.main()
