import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging
import time
import TempMail
import asyncio

class MojeIDReg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        selenium_logger = logging.getLogger('selenium')
        selenium_logger.setLevel(logging.DEBUG)

    def test_registration_form(self):
        driver = self.driver
        driver.get("https://pctuning.cz/user.sign/up")
        time.sleep(2)
        confirm_elem = driver.find_element(By.CLASS_NAME,'fc-primary-button')
        # time.sleep(2)
        confirm_elem.click()
        # time.sleep(10)
        name_elem = driver.find_element(By.ID,'frm-up-getCode-name')
        name_elem.send_keys("nameandsurname")
        # time.sleep(2)
        lastname_elem = driver.find_element(By.ID,'frm-up-getCode-username')
        lastname_elem.send_keys("Trotel1231546879")
        # time.sleep(2)
        email_elem = driver.find_element(By.ID, "frm-up-getCode-email")
        email_elem.send_keys("mojeidre1@hldrive.com")
        # time.sleep(2)
        number_elem = driver.find_element(By.ID, "frm-up-getCode-password")
        number_elem.send_keys("HT9D24[n")
        # time.sleep(2)
        number_elem = driver.find_element(By.ID, "frm-up-getCode-passwordAgain")
        number_elem.send_keys("HT9D24[n")
        # time.sleep(2)
        number_elem = driver.find_element(By.ID, "frm-up-getCode-agreeRules")
        number_elem.send_keys(Keys.SPACE)
        number_elem = driver.find_element(By.ID, "frm-up-getCode-agreePersonalData")
        number_elem.send_keys(Keys.SPACE)
        try:
            driver.find_element(By.ID, 'GAM-vv_DirectClsBtn').click()
        except:
            print("no add")
        submit_button = driver.find_element(By.NAME, "save")
        submit_button.submit()

        try:
            driver.find_element(By.ID, 'GAM-vv_DirectClsBtn').click()
        except:
            print("no add 2")
        regemail = asyncio.run(TempMail.main())
        activation_code = driver.find_element(By.ID, "frm-up-confirmCode-code")
        activation_code.send_keys(regemail)
        driver.find_element(By.NAME, "send").submit()
        time.sleep(20)
        assert "Registrace proběhla úspěšně" in driver.page_source
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
        unittest.main()