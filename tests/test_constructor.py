from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestConstructor:
    # переход к разделу "Булки"
    def test_transition_to_buns_by_click_on_button_scrolled_to_buns_section(self, driver):
        # раздел "Булки" является выбранным по умолчанию, необходимо отредактировать среду для теста
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.BUTTON_CONSTR_SAUСES))
        driver.find_element(*TestLocators.BUTTON_CONSTR_SAUСES).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.BUTTON_CONSTR_BUNS))
        driver.find_element(*TestLocators.BUTTON_CONSTR_BUNS).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.H2_BUNS))

        header_buns = driver.find_element(*TestLocators.H2_BUNS).text
        assert header_buns == 'Булки'

    # переход к разделу "Соусы"
    def test_transition_to_sauces_by_click_on_button_scrolled_to_sauces_section(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.BUTTON_CONSTR_SAUСES))
        driver.find_element(*TestLocators.BUTTON_CONSTR_SAUСES).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.H2_SAUCES))

        header_sauces = driver.find_element(*TestLocators.H2_SAUCES).text
        assert header_sauces == 'Соусы'

    # переход к разделу "Начинки"
    def test_transition_to_fillings_by_click_on_button_scrolled_to_fillings_section(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.BUTTON_CONSTR_FILLINGS))
        driver.find_element(*TestLocators.BUTTON_CONSTR_FILLINGS).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.H2_FILLINGS))

        header_fillings = driver.find_element(*TestLocators.H2_FILLINGS).text
        assert header_fillings == 'Начинки'



