from  selenium  import webdriver
from selenium.webdriver.common.by import By



chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)



driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org/")

# price_doller = driver.find_element(By.CLASS_NAME,value="a-price-whole").text
# price_cent = driver.find_element(By.CLASS_NAME,value="a-price-fraction").text
# print(price_doller)

search_bar = driver.find_element(By.NAME , value="q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID,value="submit")

print(button.size)

print(button)

documentation_link = driver.find_element(By.CSS_SELECTOR , value=".documentation-widget a")

print(documentation_link.text)
# driver.close()       # it is  usedd to close  the perticula tab of a browser# use to close all tabb  or we can say it used to close the browser

# x path  jab kuch nhi chalta toh tag ko find kerna ka liya ye har dum he kaam kerta hai

bug_link = driver.find_element(By.XPATH , value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

driver.quit()