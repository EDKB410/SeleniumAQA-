from selenium.webdriver.common.by import By


class LoginMainPage:
    ACCOUNT_DROPDOWN = (By.XPATH, "//*[@class='nav float-end']//div[@class='dropdown']")
    REGISTER = (By.XPATH, "//*[@class ='dropdown-item' and text()='Register']")
    LOGIN = (By.XPATH, "//*[@class ='dropdown-item' and text()='Login']")
    FIRSTNAME = (By.XPATH, "//input[@name='firstname']")
    LASTNAME = (By.XPATH, "//input[@name='lastname']")
    EMAIL = (By.XPATH, "//input[@name='email']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    CONTINUE_BUTTON = (By.XPATH,  "//button[@type='submit']")
    PRIVACY_POLICY_CHECKBOX = (By.XPATH, "//input[@name='agree']")
    CONGRAT_MESS = (By.XPATH, "//div[@id='content']//*[text()='Your Account Has Been Created!']")
    LOGIN_PAGE = (By.XPATH, "//div[@id='content']//*[text()='My Account']")
    LOGOUT = (By.XPATH, "//*[@class ='dropdown-item' and text()='Logout']")
    LOGOUT_PAGE = (By.XPATH, "//div[@id='content']//*[text()='Account Logout']")
    SEARCH = (By.XPATH, "//*[@id='search']/input")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='search']/button")
    ADD_TO_CART_FIRST_ITEM = (By.XPATH, "//div[@id='product-list']/div[1]//button[@title='Add to Cart']")
    SEARCH_RESULT = (By.XPATH, "//h2['Products meeting the search criteria']")
    SEARCH_FAILED = (By.XPATH, "//p[text()='There is no product that matches the search criteria.']")
    DISPLAY_CONTROL = (By.XPATH, "//div[@id='display-control']")
    CART_DROPDOWN = (By.XPATH, "//div[@class='dropdown d-grid']")
    REMOVE_POSITION = (By.XPATH, "//div[@id='shopping-cart']//tbody/tr[1]//button[2]")
    CLOSE_ALERT = (By.XPATH, "//div[@id='alert']//button")
    PRODUCT_NAME = (By.XPATH, "//div[@id='shopping-cart']//tbody/tr[1]/td[2]/a")
    MODEL = (By.XPATH, "//div[@id='shopping-cart']//tbody/tr[1]/td[3]")
    QUANTITY = (By.XPATH, "//tbody/tr[1]//input[@name='quantity']")
    UNIT_PRICE = (By.XPATH, "//div[@id='shopping-cart']//tbody/tr[1]/td[5]")
    TOTAL = (By.XPATH, "//div[@id='shopping-cart']//tbody/tr[1]/td[6]")
    CURRENCY_DROPDOWN = (By.XPATH, "//div[@class='nav float-start']//div[@class='dropdown']")
    SELECT_EUR = (By.XPATH, "//div[@class='nav float-start']//div[@class='dropdown']//a[@href='EUR']")
    SELECT_GBP = (By.XPATH, "//div[@class='nav float-start']//div[@class='dropdown']//a[@href='GBP']")
    SELECT_USD = (By.XPATH, "//div[@class='nav float-start']//div[@class='dropdown']//a[@href='USD']")
    PRICE_MAC_BOOK = (By.XPATH, "//a[text()='MacBook']/../../div/span[@class='price-new']")
    PRICE_IPHONE = (By.XPATH, "//a[text()='iPhone']/../../div/span[@class='price-new']")
    PRICE_APPLE_CINEMA = (By.XPATH, "//a[text()[contains(.,'Apple Cinema 30')]]/../../div/span[@class='price-new']")
    PRICE_CANON_5D = (By.XPATH, "//a[text()='Canon EOS 5D']/../../div/span[@class='price-new']")
    CARD_CANON_TITLE = (By.XPATH, "//div[@class='col-sm']/h1")
    REQUIRED_OPTION_SELECT = (By.XPATH, "//div[@id='product']//select/option[2]")
    ADD_TO_CART_BUTTON = (By.XPATH, "//div[@id='product']//button")
    PRICE_PRODUCT = (By.XPATH, "//div[@class='col-sm']//span[@class='price-new']")