from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Browser options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")

driver_path = 'C:\\APPS\\ChromeDriver v138\\chromedriver-win64\\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.set_window_position(0, 0)   
driver.maximize_window()
time.sleep(1)

# Initialization of the browser
driver.get('https://schoolpack.smart.edu.co/idiomas/alumnos.aspx')
time.sleep(5)

def login(USER , PASSWORD):
    #Send user and password info
    userField = driver.find_element(By.XPATH, '//*[@id="vUSUCOD"]')
    userField.send_keys(USER)
    time.sleep(2.5)

    passwordField = driver.find_element(By.XPATH, '//*[@id="vPASS"]')
    passwordField.send_keys(PASSWORD)
    time.sleep(2.5)

    #Click on confirm button
    confirmButton = driver.find_element(By.XPATH, '//*[@id="BUTTON1"]')
    confirmButton.click()
    time.sleep(5)

def closePopUp():
    pass