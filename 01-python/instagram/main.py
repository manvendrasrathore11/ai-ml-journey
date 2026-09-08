from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

SIMILAR_ACCOUNT = "lakshit.raw" # Change this to an account of your choice
USERNAME = "pythoncode54"
PASSWORD = "@1234Qwer"


class InstaFollower:

    def __init__(self):
        # Keep browser open so you can manually log out
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    # Avoid bot-like behaviour and try not to run your script too often.
    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4.2)

        # Check if the cookie warning is present on the page
        decline_cookies_xpath = '/*[@id="mount_0_0_bk"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/section/main/div/div/header/section[3]/ul/li[2]/div/a'
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            # Dismiss the cookie warning by clicking an element or button
            cookie_warning[0].click()

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2.1)
        password.send_keys(Keys.ENTER)

        time.sleep(4.3)
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3.7)
        # Click "not now" on notifications prompt
        # notifications_prompt = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        # if notifications_prompt:
        #     notifications_prompt.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        time.sleep(3)
        followers_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers/')]"))
        )
        followers_link.click()

        time.sleep(3)
        modal = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div[contains(@class, '_aano')]"))
        )

        for _ in range(5):
            # Scroll the modal
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

# /html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]
# /html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/section/main/div/div/header/section[3]/ul/li[2]/div
# /html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]