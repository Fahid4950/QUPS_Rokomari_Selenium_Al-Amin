from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\\Users\\Fahid\\Downloads\\chromedriver\\chromedriver.exe")


driver.maximize_window()



driver.get("https://www.rokomari.com/login")


driver.find_element(By.XPATH,"//*[@id='login-registration']/div/section/div[2]/div[1]/p[2]").click()
time.sleep(1)


driver.find_element(By.XPATH,"//input[@id='nm']").send_keys("Al Amin Siddique")
time.sleep(1)


driver.find_element(By.XPATH,"//input[@id='js-email']").send_keys("bappa96763@gmail.com")
time.sleep(1)

driver.find_element(By.XPATH,"//input[@id='js-phone']").send_keys("017017")
time.sleep(1)

driver.find_element(By.XPATH,"//input[@id='pwd']").send_keys("bappaarica")
time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='accountForm']/div[6]/div/div").click()
time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='accountForm']/button").send_keys(Keys.ENTER)
time.sleep(1)



