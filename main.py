from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://www.saucedemo.com/")

WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.ID, "user-name"))
)

input_element = driver.find_element(By.ID, "user-name")
# input_element1.clear()
input_element.send_keys("standard_user")
input_element = driver.find_element(By.ID, "password")
input_element.send_keys("secret_sauce")
time.sleep(5)
input_element.send_keys(Keys.ENTER)
time.sleep(10)

driver.quit()

