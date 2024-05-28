from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data.auth_data import TestAuthorizationData
from data.urls import TestUrls


class TestLogout:
    # выход по кнопке «Выйти» в личном кабинете
    def test_logout_by_click_on_button_in_personal_account_success(self, driver):
        # предусловие: вход в аккаунт
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGIN_TO_ACCOUNT))
        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_INPUT_EMAIL))
        driver.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys(TestAuthorizationData.test_login)
        driver.find_element(*TestLocators.LOGIN_INPUT_PWD).send_keys(TestAuthorizationData.test_pwd)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT))
        # шаги
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGOUT))
        driver.find_element(*TestLocators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN))

        button_text = driver.find_element(*TestLocators.BUTTON_LOGIN).text
        assert driver.current_url == TestUrls.LOGIN_PAGE and button_text == 'Войти'
