import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import asyncio
import TempMail




class MojeIDReg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_registration_form(self):
        driver = self.driver
        driver.get("https://mojeid.regtest.nic.cz/registration")
        # time.sleep(2)
        driver.find_element(By.CLASS_NAME, "tref-register-form-firstname").send_keys("Rudolf")
        # time.sleep(2)
        driver.find_element(By.CLASS_NAME, "tref-register-form-lastname").send_keys("Troll")
        # time.sleep(2)
        driver.find_element(By.ID, "email").send_keys("mojeidre1@hldrive.com")
        # time.sleep(2)
        driver.find_element(By.NAME, "telephone").send_keys("+420 723 456 789")
        # time.sleep(2)
        driver.find_element(By.CLASS_NAME,"p-checkbox-box").click()
        # time.sleep(2)
        driver.find_element(By.CLASS_NAME,"tref-register-form-submit").click()
        # time.sleep(2)
        # reg_email = asyncio.run(TempMail.main())
        time.sleep(10)
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
        unittest.main()