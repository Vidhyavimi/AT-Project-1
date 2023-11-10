import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element("name","username").send_keys("Admin")
driver.find_element("name","password").send_keys("admin123")
driver.find_element(By.XPATH,"//button").click()
driver.find_element(By.XPATH,"//a[@href='/web/index.php/pim/viewPimModule']").click()
driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active orangehrm-firstname']").send_keys("John")
driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active orangehrm-middlename']").send_keys("Joseph")
driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active orangehrm-lastname']").send_keys("paul")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(15)