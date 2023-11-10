import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element("name","username").send_keys("Admin")
driver.find_element("name","password").send_keys("admin123")
driver.find_element(By.XPATH,"//button").click()
driver.find_element(By.XPATH,"//a[@href='/web/index.php/pim/viewPimModule']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("John")
driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-trash']").click()
driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']").click()
time.sleep(15)