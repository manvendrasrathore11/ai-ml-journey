from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

SIMILAR_ACCOUNT = "pythonlearnerr"  # Change this to the account you want
USERNAME = "pythoncode54"
PASSWORD = "@1234Qwer"


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        # Handle cookies popup
        try:
            decline_button = self.driver.find_element(By.XPATH, "//button[text()='Decline optional cookies']")
            decline_button.click()
        except:
            pass  # If no cookies popup, ignore

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        # Wait for login
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Home']"))
        )

        # Dismiss save login info popup
        try:
            save_login_prompt = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Not now')]"))
            )
            save_login_prompt.click()
        except:
            pass

    def find_followers(self):
        # Open followers modal
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        # Wait for the modal to appear
        modal_xpath = "//div[@role='dialog']//div[contains(@class, '_aano')]"
        modal = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, modal_xpath))
        )

        # Dynamic scrolling until no new followers load
        last_height = 0
        while True:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(random.uniform(2, 4))
            new_height = self.driver.execute_script("return arguments[0].scrollHeight", modal)
            if new_height == last_height:
                break
            last_height = new_height

        print("All followers loaded!")

    def follow(self):
        # Find all follow buttons inside the modal
        buttons = self.driver.find_elements(By.XPATH, "//div[@role='dialog']//button[text()='Follow']")
        print(f"Found {len(buttons)} follow buttons.")

        for button in buttons:
            try:
                button.click()
                time.sleep(random.uniform(1, 3))
            except ElementClickInterceptedException:
                # If a confirmation pops up, click "Cancel"
                cancel_button = self.driver.find_element(By.XPATH, "//button[text()='Cancel']")
                cancel_button.click()
                time.sleep(1)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
