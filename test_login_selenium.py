import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://www.saucedemo.com/"
USERNAME_FIELD = (By.ID, "user-name")
PASSWORD_FIELD = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")
SUCCESS_ELEMENT = (By.ID, "inventory_container")     
ERROR_ELEMENT = (By.CSS_SELECTOR, "[data-test='error']")
SUCCESS_URL_PART = "inventory"

VALID_USER, VALID_PASS = "standard_user", "secret_sauce"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    drv = webdriver.Chrome(options=options)    
    drv.maximize_window()
    yield drv
    drv.quit()


def login(driver, username, password):
    wait = WebDriverWait(driver, 10)
    driver.get(LOGIN_URL)
    wait.until(EC.visibility_of_element_located(USERNAME_FIELD)).send_keys(username)
    wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys(password)
    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
    return wait


def test_valid_login(driver):
    wait = login(driver, VALID_USER, VALID_PASS)
    wait.until(EC.url_contains(SUCCESS_URL_PART))
    assert SUCCESS_URL_PART in driver.current_url
    assert wait.until(EC.visibility_of_element_located(SUCCESS_ELEMENT)).is_displayed()


def test_invalid_password_rejected(driver):
    wait = login(driver, VALID_USER, "wrong_password")
    error = wait.until(EC.visibility_of_element_located(ERROR_ELEMENT))
    assert "do not match" in error.text
    assert SUCCESS_URL_PART not in driver.current_url


def test_invalid_username_rejected(driver):
    wait = login(driver, "no_such_user", VALID_PASS)
    error = wait.until(EC.visibility_of_element_located(ERROR_ELEMENT))
    assert error.is_displayed()
    assert SUCCESS_URL_PART not in driver.current_url


def test_empty_credentials_rejected(driver):
    wait = login(driver, "", "")
    error = wait.until(EC.visibility_of_element_located(ERROR_ELEMENT))
    assert "required" in error.text.lower()
