from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
# import pyautogui
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
time.sleep(3)

def entryIframe():
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)

def outIframe():
    driver.switch_to.default_content()

def login(USER , PASSWORD):
    #Send user and password info
    userField = driver.find_element(By.XPATH, '//*[@id="vUSUCOD"]')
    userField.send_keys(USER)
    time.sleep(2)

    passwordField = driver.find_element(By.XPATH, '//*[@id="vPASS"]')
    passwordField.send_keys(PASSWORD)
    time.sleep(2)

    #Click on confirm button
    confirmButton = driver.find_element(By.XPATH, '//*[@id="BUTTON1"]')
    confirmButton.click()
    time.sleep(2)

def closePopUpAndClickOnSchedule():
    #Close PopUp
    popUp = driver.find_element(By.XPATH, '//*[@id="gxp0_cls"]')
    popUp.click()
    time.sleep(2)

    #Click on Schedule
    scheduleButton = driver.find_element(By.XPATH, '//*[@id="IMAGE18"]')
    scheduleButton.click()
    time.sleep(2)

def classList():
    #Click on curriculum
    curriculum = driver.find_element(By.XPATH, '//*[@id="span_W0030TMPDESART_0001"]')
    curriculum.click()
    time.sleep(2)

    #Click on init
    initButton = driver.find_element(By.XPATH, '//*[@id="W0030BUTTON1"]')
    initButton.click()
    time.sleep(2)

    entryIframe()

    #Click on select
    statusClasses = driver.find_element(By.XPATH , '//*[@id="vTPEAPROBO"]')
    select = Select(statusClasses)
    select.select_by_index(2)
    time.sleep(3)

def scheduleClass():
    #CLick on the class
    classNumber = driver.find_element(By.XPATH , "//td[contains(., 'CLASE 11')]//span[contains(text(), 'CLASE 11')]")
    classNumber.click()
    print("Logre darle click a la clase 11")
    time.sleep(3)

    #Click on asing
    asignButton = driver.find_element(By.XPATH, '//*[@id="BUTTON1"]')
    asignButton.click()
    print("Le click en asignar")
    time.sleep(3)

def scheduleBranchDayTime():
    pass