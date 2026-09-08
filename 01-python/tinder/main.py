from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

FB_PASSWORD = "@1234Qwer"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_option)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, value='//*[@id="o787701392"]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]')
fb_login.click()

sleep(2)
fb_email = driver.find_element(By.XPATH, value='//*[@id="email"]')
sleep(2)
fb_password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
fb_email.send_keys("8829804203")
fb_password.send_keys("@1234Qwer")

con = driver.find_element(By.XPATH, value='//*[@id="u_0_0_yv"]')
con.click()
