from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from logger.utils.logger_config import logger
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time

def entryIframe(driver):
    try:
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)

        logger.info("Entrar Iframe")
    except Exception as e:
        logger.error("No entre en el Iframe -> Error: {e}")

def outIframe(driver):
    try:
        driver.switch_to.default_content()
        logger.info("Salir IFrame")

    except Exception as e:
        logger.error("No logre salir del Iframe -> Error {e}")

def login(USER , PASSWORD , driver):
    try:
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
        
        logger.info("Login")
    except Exception as e:
        logger.error("Error haciendo el Login Error -> {e}")

def closePopUpAndClickOnSchedule(driver):
    try:
        #Close PopUp
        popUp = driver.find_element(By.XPATH, '//*[@id="gxp0_cls"]')
        popUp.click()
        time.sleep(2)

        #Click on Schedule
        scheduleButton = driver.find_element(By.XPATH, '//*[@id="IMAGE18"]')
        scheduleButton.click()
        time.sleep(2)

        logger.info("Cerre el PopUp")
    except Exception as e:
        logger.error("Error cerrando el PopUp Error -> {e}")

def classList(driver):
    try:
        #Click on curriculum
        curriculum = driver.find_element(By.XPATH, '//*[@id="span_W0030TMPDESART_0001"]')
        curriculum.click()
        time.sleep(2)

        #Click on init
        initButton = driver.find_element(By.XPATH, '//*[@id="W0030BUTTON1"]')
        initButton.click()
        time.sleep(2)

        entryIframe(driver)

        #Click on select
        statusClasses = driver.find_element(By.XPATH , '//*[@id="vTPEAPROBO"]')
        select = Select(statusClasses)
        select.select_by_index(2)
        time.sleep(3)

        logger.info("ClassList")
    except Exception as e:
        logger.error("Error en ClassList Error -> {e}")


def scheduleClass(driver):
    try:
        #CLick on the class
        classNumber = driver.find_element(By.XPATH , "//td[contains(., 'CLASE 11')]//span[contains(text(), 'CLASE 11')]")
        classNumber.click()
        time.sleep(3)

        #Click on asing
        asignButton = driver.find_element(By.XPATH, '//*[@id="BUTTON1"]')
        asignButton.click()
        time.sleep(3)

        outIframe(driver)

        logger.info("ScheduleClass")
    except Exception as e:
        logger.error("Error en darle Click en la clase")

def scheduleBranchDayTime(driver):
    try:
        # Buscar de nuevo los iframes después del flujo previo
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "iframe")))
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        print(f"[INFO] Total iframes encontrados: {len(iframes)}")

        iframe_correcto = None

        # Detectar iframe que contiene el elemento buscado
        for idx, iframe in enumerate(iframes):
            driver.switch_to.frame(iframe)
            if driver.find_elements(By.ID, "vREGCONREG"):  # cambia el selector si es otro
                print(f"[INFO] Elemento encontrado en iframe {idx}")
                iframe_correcto = idx
                driver.switch_to.default_content()
                break
            driver.switch_to.default_content()

        if iframe_correcto is not None:
            # Volvemos a buscar los iframes para evitar referencia inválida
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "iframe")))
            fresh_iframes = driver.find_elements(By.TAG_NAME, "iframe")
            driver.switch_to.frame(fresh_iframes[iframe_correcto])
            print(f"[INFO] Ahora estás dentro del iframe correcto {iframe_correcto}")

            # Validación para evitar error
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "vREGCONREG")))
            print("[INFO] Elemento listo para interactuar")



        else:
            print("[ERROR] No se encontró el iframe correcto.")
    except Exception as e:
        print("El error es " , e)
