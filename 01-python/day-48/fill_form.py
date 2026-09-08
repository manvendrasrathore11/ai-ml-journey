from  selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_option)
driver.get("https://secure-retreat-92358.herokuapp.com/")


First_name = driver.find_element(By.NAME , value="fName")
Last_name = driver.find_element(By.NAME , value="lName")
gmail = driver.find_element(By.NAME , value="email")



First_name.send_keys("Manvendra")
Last_name.send_keys("Singh rathore")
gmail.send_keys("manvendrasrathore@gmail.com" , Keys.ENTER)







