from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Fahid\\Downloads\\chromedriver\\chromedriver.exe")


driver.maximize_window()

driver.get("https://www.rokomari.com/book")


