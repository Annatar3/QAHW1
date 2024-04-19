from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    FIRST_NAME_INPUT = (By.ID, "firstname")
    LAST_NAME_INPUT = (By.ID, "lastname")
    EMAIL_INPUT = (By.ID, "email_address")
    PASSWORD_INPUT = (By.ID, "password")
    PASSWORD_CONFIRM_INPUT = (By.ID, "password-confirmation")
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="form-validate"]/div/div[1]/button')
    