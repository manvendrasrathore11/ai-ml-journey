from  selenium  import webdriver
from selenium.webdriver.common.by import By


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org/")

# DATE = [date.text for date in driver.find_elements(By.CLASS_NAME , value="say-no-more")]
#
# x = driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text.split("\n")
#
# event_time =
#
#
# print(x)


event_time = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a ")
event = {}

for n in range(len(event_time)):
    event[n] = {
        "time" : event_time[n].text,
        "name" : event_names[n].text,
    }
print(event)



driver.quit()