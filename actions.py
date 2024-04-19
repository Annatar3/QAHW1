from locators import RegistrationPageLocators

class RegistrationPageActions:
    def __init__(self, driver):
        self.driver = driver

    def register(self, first_name, last_name, email, password):
        self.driver.find_element(*RegistrationPageLocators.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*RegistrationPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

    def get_success_message(self):
        return self.driver.find_element(*RegistrationPageLocators.SUCCESS_MESSAGE).text
