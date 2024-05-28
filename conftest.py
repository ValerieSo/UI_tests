import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from generators import Generator


@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def registration(driver):
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

    return login_value, pwd_value
