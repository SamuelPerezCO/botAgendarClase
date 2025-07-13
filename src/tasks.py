from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")

driver_path = 'C:\\APPS\\ChromeDriver v138\\chromedriver-win64\\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.set_window_position(0, 0)   
driver.maximize_window()
time.sleep(1)

# Inicializamos el navegador
driver.get('https://schoolpack.smart.edu.co/idiomas/alumnos.aspx')
time.sleep(5)
