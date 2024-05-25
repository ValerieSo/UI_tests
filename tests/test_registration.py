from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from generators import Generator


class TestRegistration:
    # проверка возможности успешной регистрации
    def test_registration_correct_login_and_password_successful(self, driver):
        # процесс регистрации
        login_value = Generator.generate_login()
        pwd_value = Generator.generate_password()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.REGISTRATION_BUTTON_PA))
        driver.find_element(*TestLocators.REGISTRATION_BUTTON_PA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_INPUT_NAME))
        driver.find_element(*TestLocators.REGISTRATION_INPUT_NAME).send_keys('Val')
        driver.find_element(*TestLocators.REGISTRATION_INPUT_EMAIL).send_keys(login_value)
        driver.find_element(*TestLocators.REGISTRATION_INPUT_PWD).send_keys(pwd_value)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON_REG_FORM).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN))
        # повторная регистрация с тем же логином для проверки, что пользователь действительно зарегистриован
        driver.find_element(*TestLocators.REGISTRATION_BUTTON_PA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_INPUT_NAME))
        driver.find_element(*TestLocators.REGISTRATION_INPUT_NAME).send_keys('Val')
        driver.find_element(*TestLocators.REGISTRATION_INPUT_EMAIL).send_keys(login_value)
        driver.find_element(*TestLocators.REGISTRATION_INPUT_PWD).send_keys(pwd_value)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON_REG_FORM).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ERROR_USER_ALREADY_EXISTS))

        error_registration = driver.find_element(*TestLocators.ERROR_USER_ALREADY_EXISTS).text
        expected_error_text = 'Такой пользователь уже существует'
        assert error_registration == expected_error_text

    # проверка вывода сообщения об ошибке при вводе некорректного пароля
    def test_registration_incorrect_password_error_message_appears(self, driver):
        login_value = Generator.generate_login()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.REGISTRATION_BUTTON_PA))
        driver.find_element(*TestLocators.REGISTRATION_BUTTON_PA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_INPUT_NAME))
        driver.find_element(*TestLocators.REGISTRATION_INPUT_NAME).send_keys('Val')
        driver.find_element(*TestLocators.REGISTRATION_INPUT_EMAIL).send_keys(login_value)
        driver.find_element(*TestLocators.REGISTRATION_INPUT_PWD).send_keys('yes')
        driver.find_element(*TestLocators.REGISTRATION_BUTTON_REG_FORM).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ERROR_INCORRECT_PWD))

        error_registration = driver.find_element(*TestLocators.ERROR_INCORRECT_PWD).text
        expected_error_text = 'Некорректный пароль'
        assert error_registration == expected_error_text

