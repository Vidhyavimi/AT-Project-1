import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element("name","username").send_keys("Admin")
driver.find_element("name","password").send_keys("admin123")
driver.find_element(By.XPATH,"//button").click()
time.sleep(10)

try:
    driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-stopwatch']").is_displayed()
    print("The User Logged in Successfully")
except:
    print("invalid Credentails")
