import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestYandexLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_login_yandex(self):
        self.driver.get("https://passport.yandex.com/auth/")  # Change URL to yandex.com

        login_input = self.driver.find_element(By.ID, "passp-field-login")
        login_input.send_keys("YOUR_LOGIN")
        login_input.send_keys(Keys.ENTER)

        password_input = self.driver.find_element(By.ID, "passp-field-passwd")
        password_input.send_keys("YOUR_PASSWORD")
        password_input.send_keys(Keys.ENTER)

        # Wait until the "My Contacts" link becomes visible
        success_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "My Contacts"))
        )

        # Check that the "My Contacts" link is indeed visible
        self.assertTrue(success_element.is_displayed())

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

