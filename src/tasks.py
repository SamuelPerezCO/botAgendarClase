from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from logger.utils.logger_config import logger
from selenium.webdriver.common.by import By
import pyautogui
import time

def entryIframe(driver):
    try:
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)

        logger.info("ENTRE IFRAME")
    except Exception as e:
        logger.error("NO ENTRE EN EL IFRAME -> Error: {e}")

def outIframe(driver):
    try:
        driver.switch_to.default_content()
        logger.info("SALIR IFRAME")

    except Exception as e:
        logger.error("NO SALI DEL IFRAME -> Error {e}")

def login(USER , PASSWORD , driver):
    try:
        #Send user and password info
        userField = driver.find_element(By.XPATH, '//*[@id="vUSUCOD"]')
        userField.send_keys(USER)
        time.sleep(1.5)

        passwordField = driver.find_element(By.XPATH, '//*[@id="vPASS"]')
        passwordField.send_keys(PASSWORD)
        time.sleep(1.5)

        #Click on confirm button
        confirmButton = driver.find_element(By.XPATH, '//*[@id="BUTTON1"]')
        confirmButton.click()
        time.sleep(1.5)
        
        logger.info("LOGIN")
    except Exception as e:
        logger.error("ERROR INTENTANDO EL LOGIN -> {e}")

def closePopUpAndClickOnSchedule(driver):
    try:
        #Close PopUp
        popUp = driver.find_element(By.XPATH, '//*[@id="gxp0_cls"]')
        popUp.click()
        time.sleep(1.5)

        #Click on Schedule
        scheduleButton = driver.find_element(By.XPATH, '//*[@id="IMAGE18"]')
        scheduleButton.click()
        time.sleep(1.5)

        logger.info("CERRE EL POPUP -> CLICK EN AGENDAR")
    except Exception as e:
        logger.error("ERROR CERRANDO EL POPUP : Error -> {e}")

def classList(driver):
    try:
        #Click on curriculum
        curriculum = driver.find_element(By.XPATH, '//*[@id="span_W0030TMPDESART_0001"]')
        curriculum.click()
        time.sleep(1.5)

        #Click on init
        initButton = driver.find_element(By.XPATH, '//*[@id="W0030BUTTON1"]')
        initButton.click()
        time.sleep(1.5)

        entryIframe(driver)

        #Click on select
        statusClasses = driver.find_element(By.XPATH , '//*[@id="vTPEAPROBO"]')
        select = Select(statusClasses)
        select.select_by_index(2)
        time.sleep(1.5)

        logger.info("LISTA DE CLASES")
    except Exception as e:
        logger.error("ERROR EN LA LISTA DE CLASES: Error -> {e}")

#Se recibe la clase
def scheduleClass(driver , clase):
    try:
        #CLick on the class
        classNumber = driver.find_element(By.XPATH , f"//td[contains(., '{clase}')]//span[contains(text(), '{clase}')]")
        classNumber.click()
        time.sleep(1.5)

        #Click on asing
        asignButton = driver.find_element(By.XPATH, '//*[@id="BUTTON1"]')
        asignButton.click()
        time.sleep(1.5)

        outIframe(driver)

        logger.info("AGENDAR CLASE")
    except Exception as e:
        logger.error("ERROR DANDOLE CLICK EN LA CLASE")

#Me recibe Branch , Dia , HORA
def scheduleBranchDayTime(driver , sede , dia , hora):
    try:
        # Buscar de nuevo los iframes después del flujo previo
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "iframe")))
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        logger.info(f"Total iframes encontrados: {len(iframes)}")

        iframe_correcto = None

        # Detectar iframe que contiene el elemento buscado
        for idx, iframe in enumerate(iframes):
            driver.switch_to.frame(iframe)
            if driver.find_elements(By.ID, "vREGCONREG"): 
                logger.info(f"Elemento encontrado en iframe {idx}")
                iframe_correcto = idx
                driver.switch_to.default_content()
                break
            driver.switch_to.default_content()

        if iframe_correcto is not None:
            # Volvemos a buscar los iframes para evitar referencia inválida
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "iframe")))
            fresh_iframes = driver.find_elements(By.TAG_NAME, "iframe")
            driver.switch_to.frame(fresh_iframes[iframe_correcto])
            logger.info(f"Ahora estás dentro del iframe correcto {iframe_correcto}")

            # Validación para evitar error
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "vREGCONREG")))
            logger.info("Elemento listo para interactuar")

        else:
            logger.error("No se encontró el iframe correcto.")

        #Seleccionar la sede
        branchList = driver.find_element(By.XPATH , '//*[@id="vREGCONREG"]')
        select = Select(branchList)
        #Aca selecciona la sede
        select.select_by_visible_text(f"{sede}")
        logger.info("SEDE SELECCIONADA")
        time.sleep(1.5)

        #Seleccionar el Dia
        dayList = driver.find_element(By.XPATH, '//*[@id="vDIA"]')
        select = Select(dayList)
        select.select_by_visible_text(f"{dia}")
        logger.info("DIA SELECCIONADO")
        time.sleep(1.5)

        #Cambia segun la clase que necesito
        classHour = driver.find_element(By.XPATH , f"{hora}")
        classHour.click()
        logger.info("HORA SELECCIONADA")
        time.sleep(1.5)

        confirmButton = driver.find_element(By.XPATH, '//*[@id="BUTTON1"]')
        confirmButton.click()
        logger.info("CLICK EN CONFIRMAR")
        time.sleep(1.5)
    except Exception as e:
        logger.error(f"ERROR ES: {e} ")
        time.sleep(1.5)

def outOfWebPage(driver):
    outIframe(driver)

    rutaImagenXbutton = 'C:\\Codigos\\botAgendarClase\\src\\imgs\\xButton.png'

    ubicacionXbutton = pyautogui.locateOnScreen(rutaImagenXbutton , confidence= 0.8)

    if ubicacionXbutton:
        centro = pyautogui.center(ubicacionXbutton)
        pyautogui.click(centro)
        time.sleep(1.5)
    else:
        logger.error("IMAGEN NO ENCONTRADA")
        time.sleep(4)

    
    time.sleep(3)
    
    driver.find_element(By.ID, "SALIR").click()
    alert = Alert(driver)
    alert.accept() 
