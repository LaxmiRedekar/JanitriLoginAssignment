import os

from selenium import webdriver
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)


def setup_driver():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://dev-dash.janitri.in/")
    driver.maximize_window()
    return driver


def email_query(wait):
    email = wait.until(EC.presence_of_element_located((By.ID, "formEmail")))
    return email


def password_query(wait):
    pwd = wait.until(EC.presence_of_element_located((By.ID, "formPassword")))
    return pwd


def error_message(wait):
    error = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "normal-text"))).text
    return error


def login_button(wait):
    login = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login-button")))
    return login


def test_valid_login(email, password, login, wait):
    # Test case 1: valid email and password
    try:
        email.send_keys("laxmiredekar07@gmail.com")
        password.send_keys("laxmi")
        login.click()
        error_msg = error_message(wait)
        print(error_msg)
    except NoSuchElementException:
        print("Username field not found on the page.")


def test_missing_email(email, password, login, wait):
    # Test case 2: Missing email
    try:
        email.clear()
        password.clear()
        password.send_keys("laxmi")
        login.click()
        error_msg = error_message(wait)
        print(error_msg)
    except NoSuchElementException:
        print("Username field not found on the page.")


def test_missing_pwd(email, password, login, wait,driver):
    # Test case 3: Missing password
    email.clear()
    email.send_keys("laxmi@gmail.com")
    password.clear()
    login.click()
    error_msg = error_message(wait)
    print(error_msg)
    time.sleep(5)
    driver.save_screenshot(os.getcwd() + "\\missing_pwd.png")


def test_missing_emailpwd(email, password, login, wait):
    # Test case 4: when password and email is not passed
    email.clear()
    password.clear()
    login.click()
    error_msg = error_message(wait)
    print(error_msg)


def test_masking(driver, password):
    # Test case 5: validate password masking
    password.send_keys("laxmi")
    driver.find_element(By.CLASS_NAME, "passowrd-visible").click()
    time.sleep(5)
    driver.save_screenshot(os.getcwd() + "\\toggle.png")


def test_email_pattern(email, password, login, waiit):
    # Test case 6: wrong email pattern
    email.clear()
    email.send_keys("laxmi#gmail/com")
    password.clear()
    password.send_keys("1111")
    login.click()
    error_msg = error_message(waiit)
    print(error_msg)


def test_case_sensitive(email, password, login, wait):
    # test case 7: checking for case-sensitive email
    email.send_keys("LAXMI@GMAIL.COM")
    password.send_keys("1111")
    login.click()
    error_msg = error_message(wait)
    print(error_msg)


def test_password_toggle(password, driver):
    # Test case 8: Checking for after masking will the value change or not
    pwd = "laxmi"
    password.send_keys(pwd)

    mask_value = password.get_attribute("value")

    toggle = driver.find_element(By.CLASS_NAME, "passowrd-visible")
    toggle.click()
    time.sleep(5)

    unmasked_value = password.get_attribute("value")
    if mask_value == unmasked_value:
        print("After masking value does not change")
    else:
        print("After masking value change")


def main():
    driver = setup_driver()
    wait = WebDriverWait(driver, 20)
    email = email_query(wait)
    pwd = password_query(wait)
    login = login_button(wait)

    # Run test cases
    test_valid_login(email, pwd, login,wait)
    time.sleep(5)

    test_missing_email(email, pwd, login, wait)
    time.sleep(5)

    test_missing_pwd(email, pwd, login, wait, driver)
    time.sleep(5)

    test_missing_emailpwd(email, pwd, login, wait)
    time.sleep(5)

    test_masking(driver, pwd)
    time.sleep(5)

    test_email_pattern(email, pwd, login, wait)
    time.sleep(5)

    test_case_sensitive(email, pwd, login, wait)
    time.sleep(5)

    test_password_toggle(pwd, driver)
    time.sleep(5)


if __name__ == "__main__":
    main()
