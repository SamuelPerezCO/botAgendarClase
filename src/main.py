from logger.utils.logger_config import logger
from config import USER , PASSWORD
import confirmMessage
import driver_setup
import tasks
import json
import power
import time



# Leer desde el archivo y enviar los datos
with open("clases.txt", "r") as archivo:
    clases_leidas = json.load(archivo)

if not clases_leidas:
    logger.info("NO HAY CLASES PARA ASIGNAR -> APAGANDO")
    power.shutdowm()
    exit()


logger.info("-" * 25 + "INICIO" + "-" * 25)

for numero_clase , detalles in clases_leidas.items():
    driver = driver_setup.setup()

    tasks.login(USER ,PASSWORD ,driver)
    tasks.closePopUpAndClickOnSchedule(driver)
    tasks.classList(driver)
    tasks.scheduleClass(driver , numero_clase)
    tasks.scheduleBranchDayTime(driver, detalles["sede"] , detalles["dia"] , detalles["hora"])
    tasks.outOfWebPage(driver)
    logger.info(f"{numero_clase} ASIGNADA")

confirmMessage.sendMessage()
time.sleep(10)
power.shutdowm()

logger.info("-" * 25 + "FIN" + "-" * 25)
