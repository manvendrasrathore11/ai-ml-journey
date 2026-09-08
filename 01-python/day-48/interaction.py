# from  selenium  import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_experimental_option("detach",True)
#
#
#
# driver = webdriver.Chrome(options=chrome_option)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# #
# # total_articles = driver.find_element(By.XPATH , value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# #
# # total_articles.click()
#
# # all_portals = driver.find_element(By.LINK_TEXT , value="Content portals")
#
# # all_portals.click()
#
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# ✅ Wait until the search box is clickable
wait = WebDriverWait(driver, 10)
search = wait.until(EC.element_to_be_clickable((By.NAME, "search")))

# ✅ Now it's safe to send keys
search.send_keys("Python")
search.send_keys(Keys.RETURN)
