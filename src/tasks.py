from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time

# Opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\APPS\\ChromeDriver\\chromedriver-win64\\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options = options)

driver.set_window_position(2000 , 0)
driver.maximize_window()
time.sleep(1)