# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Optional: Keep browser open after script finishes
# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_experimental_option("detach", True)
#
# # Launch browser
# driver = webdriver.Chrome(options=chrome_option)
# driver.get("https://ozh.github.io/cookieclicker/")
#
# # Wait for the language button to be visible (wait up to 15 seconds)
# wait = WebDriverWait(driver, 15)
# select_language = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
#
# # Now you can click or press enter
# select_language.click()  # OR: select_language.send_keys(Keys.ENTER)

from time import sleep,time

start = time()

print(start)