import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException

# Load your login credentials from environment variables
stake_username = os.getenv('STAKE_USERNAME')
stake_password = os.getenv('STAKE_PASSWORD')

zula_username = os.getenv('ZULA_USERNAME')
zula_password = os.getenv('ZULA_PASSWORD')

mcluck_username = os.getenv('MCLUCK_USERNAME')
mcluck_password = os.getenv('MCLUCK_PASSWORD')

modo_username = os.getenv('MODO_USERNAME')
modo_password = os.getenv('MODO_PASSWORD')

fortune_coins_username = os.getenv('FORTUNE_COINS_USERNAME')
fortune_coins_password = os.getenv('FORTUNE_COINS_PASSWORD')

global_poker_username = os.getenv('GLOBAL_POKER_USERNAME')
global_poker_password = os.getenv('GLOBAL_POKER_PASSWORD')

high5casino_username = os.getenv('HIGH5CASINO_USERNAME')
high5casino_password = os.getenv('HIGH5CASINO_PASSWORD')

ding_ding_ding_username = os.getenv('DING_DING_DING_USERNAME')
ding_ding_ding_password = os.getenv('DING_DING_DING_PASSWORD')

chumba_username = os.getenv('CHUMBA_USERNAME')
chumba_password = os.getenv('CHUMBA_PASSWORD')

no_limit_coins_username = os.getenv('NO_LIMIT_COINS_USERNAME')
no_limit_coins_password = os.getenv('NO_LIMIT_COINS_PASSWORD')

wow_vegas_username = os.getenv('WOW_VEGAS_USERNAME')
wow_vegas_password = os.getenv('WOW_VEGAS_PASSWORD')

# Initialize the Chrome driver
driver = webdriver.Chrome()

def login(url, username, password, login_steps):
    driver.get(url)
    print(f"Navigating to {url}")

    for step in login_steps:
        action = step['action']
        locator = step['locator']
        value = step.get('value')
        attempts = 3  # Number of retry attempts for each action

        for attempt in range(attempts):
            try:
                if action == "click":
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator)).click()
                    print(f"Clicked on {locator}.")
                elif action == "send_keys":
                    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(locator)).send_keys(value)
                    print(f"Entered credentials for {locator}.")
                elif action == "check_exists":
                    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(locator))
                    print(f"Verified element existence for {locator}.")
                break  # Exit the retry loop if successful
            except (TimeoutException, StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException) as e:
                print(f"Error during {action} on {locator}: {e}")
                if attempt == attempts - 1:
                    print(f"Giving up on {locator} after {attempts} attempts.")
                time.sleep(1)  # Wait a bit before retrying

def main():
    login_to_stake_steps = [
        {'action': 'click', 'locator': (By.XPATH, "//button[@data-testid='login-link']")}, 
        {'action': 'send_keys', 'locator': (By.NAME, "emailOrName"), 'value': stake_username},
        {'action': 'send_keys', 'locator': (By.NAME, "password"), 'value': stake_password + Keys.RETURN}
    ]
    
    login_to_zula_steps = [
        {'action': 'click', 'locator': (By.ID, "accept-btn")},
        {'action': 'click', 'locator': (By.ID, "TEST_LOADING_BUTTON")},
        {'action': 'send_keys', 'locator': (By.NAME, "username"), 'value': zula_username},
        {'action': 'send_keys', 'locator': (By.NAME, "password"), 'value': zula_password},
        {'action': 'click', 'locator': (By.ID, "TEST_LOADING_BUTTON")}
    ]
    
    login_to_mcluck_steps = [
        {'action': 'click', 'locator': (By.XPATH, "//a[@data-test='header-login-btn']")},
        {'action': 'custom_action', 'locator': (By.XPATH, "//input[@type='checkbox']")},  
        {'action': 'send_keys', 'locator': (By.NAME, "username"), 'value': mcluck_username},
        {'action': 'send_keys', 'locator': (By.NAME, "password"), 'value': mcluck_password},
        {'action': 'click', 'locator': (By.CLASS_NAME, "recaptcha-checkbox-border")}, 
        {'action': 'click', 'locator': (By.XPATH, "//button[@data-test='login-now-btn']")}
    ]

    login_to_modo_steps = [
        {'action': 'click', 'locator': (By.CLASS_NAME, "loginFormButtton")},
        {'action': 'send_keys', 'locator': (By.NAME, "username"), 'value': modo_username},
        {'action': 'send_keys', 'locator': (By.NAME, "password"), 'value': modo_password},
        {'action': 'click', 'locator': (By.CLASS_NAME, "recaptcha-checkbox-border")},
        {'action': 'click', 'locator': (By.ID, "1-submit")}
    ]

    login_to_fortune_coins_steps = [
        {'action': 'click', 'locator': (By.CLASS_NAME, "loadingBtn")},
        {'action': 'send_keys', 'locator': (By.NAME, "username"), 'value': fortune_coins_username},
        {'action': 'send_keys', 'locator': (By.NAME, "password"), 'value': fortune_coins_password},
        {'action': 'click', 'locator': (By.CLASS_NAME, "loginFormButtton")}
    ]

    login_to_global_poker_steps = [
        {'action': 'click', 'locator': (By.XPATH, "//a[@href='/login']")},
        {'action': 'send_keys', 'locator': (By.NAME, "username"), 'value': global_poker_username},
        {'action': 'send_keys', 'locator': (By.NAME, "password"), 'value': global_poker_password},
        {'action': 'click', 'locator': (By.XPATH, "//span[contains(text(), 'Log In')]")}
    ]

    login_to_high5casino_steps = [
        {'action': 'click', 'locator': (By.CLASS_NAME, "login-btn")},
        {'action': 'click', 'locator': (By.CLASS_NAME, "buttonTextWhite")},
        {'action': 'send_keys', 'locator': (By.NAME, "username"), 'value': high5casino_username},
        {'action': 'send_keys', 'locator': (By.NAME, "password"), 'value': high5casino_password},
        {'action': 'click', 'locator': (By.CLASS_NAME, "signInButtonPopup")}
    ]

    login_to_ding_ding_ding_steps = [
        {'action': 'click', 'locator': (By.CLASS_NAME, "btn--outline")},
        {'action': 'send_keys', 'locator': (By.NAME, "username"), 'value': ding_ding_ding_username},
        {'action': 'send_keys', 'locator': (By.NAME, "password"), 'value': ding_ding_ding_password},
        {'action': 'click', 'locator': (By.CLASS_NAME, "recaptcha-checkbox-border")},
        {'action': 'click', 'locator': (By.XPATH, "//div[contains(text(), 'Login')]")}
    ]

    login_to_chumba_steps = [
        {'action': 'click', 'locator': (By.XPATH, "//a[contains(text(), 'Log In')]")},
        {'action': 'send_keys', 'locator': (By.NAME, "username"), 'value': chumba_username},
        {'action': 'send_keys', 'locator': (By.NAME, "password"), 'value': chumba_password},
        {'action': 'click', 'locator': (By.XPATH, "//button[contains(text(), 'Log In')]")}
    ]

    login_to_no_limit_coins_steps = [
        {'action': 'click', 'locator': (By.XPATH, "//button[contains(text(), 'Log In')]")},
        {'action': 'send_keys', 'locator': (By.NAME, "username"), 'value': no_limit_coins_username},
        {'action': 'send_keys', 'locator': (By.NAME, "password"), 'value': no_limit_coins_password},
        {'action': 'click', 'locator': (By.XPATH, "//button[contains(text(), 'Log In')]")}
    ]

    login_to_wow_vegas_steps = [
        {'action': 'click', 'locator': (By.XPATH, "//a[contains(text(), 'Login')]")},
        {'action': 'send_keys', 'locator': (By.NAME, "username"), 'value': wow_vegas_username},
        {'action': 'send_keys', 'locator': (By.NAME, "password"), 'value': wow_vegas_password},
        {'action': 'click', 'locator': (By.XPATH, "//button[contains(text(), 'Log In')]")}
    ]

    # Call login function for each site
    login("https://stake.us", stake_username, stake_password, login_to_stake_steps)
    login("https://www.zulacasino.com/", zula_username, zula_password, login_to_zula_steps)
    login("https://www.mcluck.com/home", mcluck_username, mcluck_password, login_to_mcluck_steps)
    login("https://www.modo.com", modo_username, modo_password, login_to_modo_steps)
    login("https://www.fortunecoins.com", fortune_coins_username, fortune_coins_password, login_to_fortune_coins_steps)
    login("https://www.globalpoker.com", global_poker_username, global_poker_password, login_to_global_poker_steps)
    login("https://www.high5casino.com", high5casino_username, high5casino_password, login_to_high5casino_steps)
    login("https://www.dingdingding.com", ding_ding_ding_username, ding_ding_ding_password, login_to_ding_ding_ding_steps)
    login("https://www.chumba.com", chumba_username, chumba_password, login_to_chumba_steps)
    login("https://www.nolimitcoins.com", no_limit_coins_username, no_limit_coins_password, login_to_no_limit_coins_steps)
    login("https://www.wowvegas.com", wow_vegas_username, wow_vegas_password, login_to_wow_vegas_steps)

    # Optional: Close the browser after all logins
    driver.quit()

if __name__ == "__main__":
    main()
