from asyncio import sleep

from  selenium  import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,time


start = time()
Five_min = time() + 300
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://ozh.github.io/cookieclicker/")

def find_option():
    options = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    print(options)
    if options:
        # Do something if options are found
        print(f"{len(options)} options found")
        options[-1].click()



sleep(3)

try :

    select_language = driver.find_element(By.ID , value="langSelect-EN")
    select_language.click()
    sleep(3)

except NoSuchElementException :
    print("Language selection not found")


sleep(2)

cookie = driver.find_element(By.ID , value="bigCookie")
while True:
    cookie.click()
    if time() - start >= 5:
        find_option()
        start = time()

    if time() >= Five_min:
        sleep(5)
        driver.quit()






