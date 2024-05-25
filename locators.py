from selenium.webdriver.common.by import By


class TestLocators:
    # кнопка "Личный кабинет"
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    # кнопка "Зарегистрироваться" в личном кабинете
    REGISTRATION_BUTTON_PA = (By.XPATH, "//a[text()='Зарегистрироваться']")
    # поле ввода "Имя" при регистрации
    REGISTRATION_INPUT_NAME = (By.XPATH, "//*[text()='Имя']/following-sibling::input")
    # поле ввода "Email" при регистрации
    REGISTRATION_INPUT_EMAIL = (By.XPATH, "//*[text()='Email']/following-sibling::input")
    # поле ввода "Пароль" при регистрации
    REGISTRATION_INPUT_PWD = (By.XPATH, "//*[text()='Пароль']/following-sibling::input")
    # кнопка"Зарегистрироваться" в форме регистрации
    REGISTRATION_BUTTON_REG_FORM = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # кнопка "Войти" на странице авторизации
    BUTTON_LOGIN = (By.XPATH, "//form/button[text()='Войти']")
    # сообщение об ошибке при регистрации с тем же логином
    ERROR_USER_ALREADY_EXISTS = (By.XPATH, "//p[text()='Такой пользователь уже существует']")
    # сообщение об ошибке при вводе невалидного пароля в форму регистрации
    ERROR_INCORRECT_PWD = (By.XPATH, "//p[text()='Некорректный пароль']")
    # кнопка "Войти в аккаунт" на главной странице
    BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # поле ввода "Email" на странице авторизации
    LOGIN_INPUT_EMAIL = (By.XPATH, "//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    # поле ввода "Пароль" на странице авторизации
    LOGIN_INPUT_PWD = (By.XPATH, "//input[@type = 'password']")
    # кнопка "Оформить заказ" на главной странице
    BUTTON_ORDER = (By.XPATH, "//button[text() = 'Оформить заказ']")
    # кнопка "Войти" в форме регистрации/ восстановления пароля
    lOGIN_lINK_REG_FORM = (By.XPATH, "//a[text()='Войти']")
    # кнопка "Восстановить пароль"
    RESTORE_PWS_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    # кнопка "Профиль"
    BUTTON_PROFILE = (By.XPATH, "//a[text() = 'Профиль']")
    # поле "Логин" профиля в ЛК
    PROFILE_LOGIN_INPUT = (By.XPATH, "//label[text()= 'Логин']/following-sibling::input")
    # кнопка "Конструктор"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    # логотип Stellar Burgers
    LOGO_STELLAR_BURGERS = (By.XPATH, ".//body//div[@class='AppHeader_header__logo__2D0X2']")
    # кнопка "Выйти" в ЛК
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")
    # кнопка "Булки" в конструкторе
    BUTTON_CONSTR_BUNS = (By.XPATH, "//span[text() ='Булки']")
    # кнопка "Соусы" в конструкторе
    BUTTON_CONSTR_SAUСES = (By.XPATH, "//span[text() ='Соусы']")
    # кнопка "Начинки" в конструкторе
    BUTTON_CONSTR_FILLINGS = (By.XPATH, "//span[text() ='Начинки']")
    # Заголовок "БУЛКИ" в ленте выбора конструктора
    H2_BUNS = (By.XPATH, "//h2[text()='Булки']")
    # Заголовок "Соусы" в ленте выбора конструктора
    H2_SAUCES = (By.XPATH, "//h2[text()='Соусы']")
    # Заголовок "Начинки" в ленте выбора конструктора
    H2_FILLINGS = (By.XPATH, "//h2[text()='Начинки']")


