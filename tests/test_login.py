from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data.auth_data import TestAuthorizationData
from data.urls import TestUrls


class TestLogin:
    # проверка возможности входа в аккаунт по кнопке «Войти в аккаунт» на главной
    def test_login_by_click_on_login_button_on_main_success(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGIN_TO_ACCOUNT))
        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_INPUT_EMAIL))
        driver.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys(TestAuthorizationData.test_login)
        driver.find_element(*TestLocators.LOGIN_INPUT_PWD).send_keys(TestAuthorizationData.test_pwd)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER))

        order_button = driver.find_element(*TestLocators.BUTTON_ORDER)
        assert order_button.text == 'Оформить заказ' and driver.current_url == TestUrls.MAIN_PAGE

    # проверка возможности входа в аккаунт через кнопку «Личный кабинет»
    def test_login_from_personal_account_success(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_INPUT_EMAIL))
        driver.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys(TestAuthorizationData.test_login)
        driver.find_element(*TestLocators.LOGIN_INPUT_PWD).send_keys(TestAuthorizationData.test_pwd)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER))

        order_button = driver.find_element(*TestLocators.BUTTON_ORDER)
        assert order_button.text == 'Оформить заказ' and driver.current_url == TestUrls.MAIN_PAGE

    # проверка возможности входа в аккаунт через кнопку в форме регистрации
    def test_login_registration_form_sign_in_button_success(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.REGISTRATION_BUTTON_PA))
        driver.find_element(*TestLocators.REGISTRATION_BUTTON_PA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.lOGIN_lINK_REG_FORM))
        driver.find_element(*TestLocators.lOGIN_lINK_REG_FORM).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_INPUT_EMAIL))
        driver.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys(TestAuthorizationData.test_login)
        driver.find_element(*TestLocators.LOGIN_INPUT_PWD).send_keys(TestAuthorizationData.test_pwd)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER))

        order_button = driver.find_element(*TestLocators.BUTTON_ORDER)
        assert order_button.text == 'Оформить заказ' and driver.current_url == TestUrls.MAIN_PAGE

    # проверка возможности входа в аккаунт через кнопку в форме восстановления пароля
    def test_login_button_on_the_password_recovery_form_success(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGIN_TO_ACCOUNT))
        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.RESTORE_PWS_LINK))
        driver.find_element(*TestLocators.RESTORE_PWS_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.lOGIN_lINK_REG_FORM))
        driver.find_element(*TestLocators.lOGIN_lINK_REG_FORM).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_INPUT_EMAIL))
        driver.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys(TestAuthorizationData.test_login)
        driver.find_element(*TestLocators.LOGIN_INPUT_PWD).send_keys(TestAuthorizationData.test_pwd)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER))

        order_button = driver.find_element(*TestLocators.BUTTON_ORDER)
        assert order_button.text == 'Оформить заказ' and driver.current_url == TestUrls.MAIN_PAGE
