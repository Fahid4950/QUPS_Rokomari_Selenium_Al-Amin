import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path="C:\\Users\\Fahid\\Downloads\\chromedriver\\chromedriver.exe")

driver.maximize_window()



driver.get("https://www.rokomari.com/login")


driver.find_element(By.XPATH,"//input[@id='j_username']").send_keys("bappa9673@gmail.com")
time.sleep(1)

driver.find_element(By.XPATH,"//input[@id='j_password']").send_keys("bappaarica")
time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='loginForm']/button").send_keys(Keys.ENTER)
time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='dropdownMenu2']").click()
time.sleep(1)


driver.find_element(By.XPATH,"/html/body/header/div/div/div/div/div[3]/div/div[3]/div/a[7]").click()





