import unittest
from selenium import webdriver
#from locators import RegistrationPageLocators
from actions import RegistrationPageActions

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://magento.softwaretestingboard.com/customer/account/create/')
        self.registration_actions = RegistrationPageActions(self.driver)

    def tearDown(self):
        self.driver.quit()  

    def test_registration_success(self):
        self.registration_actions.register("Nika", "Demchenko", "nikoloz.demchenko.1@btu.edu.ge", "Pa$$w0rd")
        success_message = self.registration_actions.get_success_message()
        self.assertIn("Thank you for registering with Main Website Store.", success_message)

if __name__ == "__main__":
    unittest.main()
