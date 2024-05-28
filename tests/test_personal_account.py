from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestPersonalAccount:
    # проверка возможности входа в личный кабинет по кнопке «Личный Кабинет» на главной
    def test_personal_account_button(self, driver, registration):
        # предусловие: вход в аккаунт
        login_value, pwd_value = registration
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_INPUT_EMAIL))
        driver.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys(login_value)
        driver.find_element(*TestLocators.LOGIN_INPUT_PWD).send_keys(pwd_value)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        # шаги
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_PROFILE))

        login_input_value = driver.find_element(*TestLocators.PROFILE_LOGIN_INPUT).get_attribute('value')
        assert login_input_value == login_value

    # переход из личного кабинета в конструктор по клику на кнопку "Конструктор"
    def test_transition_to_constructor_by_click_on_button_success(self, driver, registration):
        # предусловие: вход в аккаунт
        login_value, pwd_value = registration
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_INPUT_EMAIL))
        driver.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys(login_value)
        driver.find_element(*TestLocators.LOGIN_INPUT_PWD).send_keys(pwd_value)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        # шаги
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.BUTTON_CONSTRUCTOR))
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()

        order_button = driver.find_element(*TestLocators.BUTTON_ORDER)
        assert order_button.text == 'Оформить заказ' and driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
    def test_transition_to_constructor_by_click_on_logo_success(self, driver, registration):
        # предусловие: переход на главную страницу после регистрации
        login_value, pwd_value = registration
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_INPUT_EMAIL))
        driver.find_element(*TestLocators.LOGIN_INPUT_EMAIL).send_keys(login_value)
        driver.find_element(*TestLocators.LOGIN_INPUT_PWD).send_keys(pwd_value)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        # шаги
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.LOGO_STELLAR_BURGERS))
        driver.find_element(*TestLocators.LOGO_STELLAR_BURGERS).click()

        order_button = driver.find_element(*TestLocators.BUTTON_ORDER)
        assert order_button.text == 'Оформить заказ' and driver.current_url == 'https://stellarburgers.nomoreparties.site/'
