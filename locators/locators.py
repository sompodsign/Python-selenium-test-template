from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    CAPTCHA_FRAME = (By.XPATH, "//iframe[@title='reCAPTCHA']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Sign In')]")
    CAPTCHA_CHECK_BOX = (By.XPATH, "//*[@id=\"recaptcha-anchor\"]/div[1]")


class HomePageLocators:
    # TOP NAVIGATION
    LOGO = (By.XPATH, "//div[@class='col-auto']//*[name()='svg']")
    DOGS_MENU = (By.XPATH, "//a[normalize-space()='DOGS']")
    RACES_MENU = (By.XPATH, "//a[normalize-space()='RACES']")
    MARKETPLACE_MENU = (By.XPATH, "//a[normalize-space()='RACES']")
    ABOUT_MENU = (By.XPATH, "//a[normalize-space()='ABOUT']")
    SIGN_UP_BTN = (By.XPATH, "//button[contains(text(),'SIGN IN • UP')]")
    CONNECT_WALLET_BTN = (By.XPATH, "//button[normalize-space()='CONNECT WALLET']")

    # HERO SECTION
    MAIN_HERO_TEXT = (By.XPATH, "//h1[normalize-space()='Make money by racing dogs']")
    SUB_HERO_TEXT = (By.XPATH, "//p[@class='sc-giYglK bDwXye']")
    GET_STARTED_BTN = (By.XPATH, "//button[normalize-space()='GET STARTED']")
    JOIN_AND_BUY_SECTION = (By.XPATH, "//div[@class='sc-ikJyIC ektmRX']")
    JOIN_TEXT = (By.XPATH, "//p[contains(text(),'time to bet on your favorite! Pimp your DOG$,')]")
    BUY_RACE_COURSES = (By.XPATH, "//div[@class='swiper-slide swiper-slide-active']//h3[@class='sc-hiCibw gYOHnn']["
                                  "normalize-space()='BUY RACE COURSES']")
    HERO_SECTION_NEXT_BTN = (By.XPATH, "//button[@class='sc-iqseJM sc-jcFjpl jwxEYR epdPwn']")

    # Champions club section
    CHAMPIONS_HEADER = (By.XPATH, "//h2[contains(.,'Join the new world champions club')]")
    NFT_DOGS_CARD = (By.XPATH, "//h3[normalize-space()='UNIQUE NFT GREYHOUND DOGS']")
    MARKETPLACE_CARD = (By.XPATH, "//h3[normalize-space()='NFT METARACE MARKETPLACE']")
    RACE_CARD = (By.XPATH, "//h3[normalize-space()='RACE']")
    EXPLORE_NFT_DOGS_BTN = (By.XPATH, "//button[normalize-space()='EXPLORE NFT DOGS']")
    ACQUIRE_DOG_BTN = (By.XPATH, "//button[normalize-space()='AQUIRE DOG$']")
    JOIN_RACES_CARD_BTN = (By.XPATH, "//button[normalize-space()='AQUIRE DOG$']")

    # Story section
    STORY_SECTION_HEADER = (By.XPATH, "//h2[normalize-space()='Our story starts now']")
    STORY_CARDS = (By.XPATH, "//h2[normalize-space()='Our story starts now']//parent::div/following-sibling::div")

    # Subscribe Section
    SUBSCRIBE_NOW_TEXT = (By.XPATH, "//h3[normalize-space()='SUBSCRIBE NOW']")
    JOIN_META_DOG_TEXT = (By.XPATH, "//h2[normalize-space()='Join Metadog Race community!']")
    SUBSCRIBE_EMAIL_INPUT_FIELD = (
    By.XPATH, "//h2[normalize-space()='Join Metadog Race community!']//parent::div/following-sibling::div//form//input")
    SUBSCRIBE_BTN = (By.XPATH, "//button[normalize-space()='SUBSCRIBE']")

    # footer section
    FOOTER_LOGO = (
    By.XPATH, "(((//div[@class='sc-hGPBjI bQZxYx']//parent::div//parent::div)[1]//child::div[1])[1]//*)[1]")
    FOOTER_MENU_ITEMS = (By.XPATH, "//div[@class='sc-hGPBjI bQZxYx']//div")
    COPYRIGHT_TEXT = (By.XPATH, "//p[@class='sc-cxpSdN cVpCsr']")
