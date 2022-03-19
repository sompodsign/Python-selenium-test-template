from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    CAPTCHA_FRAME = (By.XPATH, "//iframe[@title='reCAPTCHA']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Sign In')]")
    CAPTCHA_CHECK_BOX = (By.XPATH, "//*[@id=\"recaptcha-anchor\"]/div[1]")


class HomePageLocators:
    WELCOME_MESSAGE = (By.XPATH, "//h5[normalize-space()='Unidevgo Test']")