"""Script principal para automatizar la asignación de clases.

Este script:
    1. Lee las clases pendientes desde un archivo JSON (`clases.txt`).
    2. Si no hay clases, apaga el equipo.
    3. Si hay clases, abre el navegador, inicia sesión y realiza el flujo de:
        - Cerrar pop-up inicial.
        - Acceder a la lista de clases.
        - Seleccionar clase.
        - Seleccionar sede, día y hora.
        - Salir de la página.
    4. Envía un mensaje de confirmación.
    5. Apaga el equipo.

Modules:
    logger.utils.logger_config: Configuración y uso de logs.
    config: Variables de configuración como usuario y contraseña.
    confirmMessage: Envío de mensaje de confirmación al finalizar.
    driver_setup: Configuración del WebDriver.
    tasks: Funciones de automatización con Selenium.
    json: Lectura de datos desde archivo JSON.
    power: Apagado del sistema.
    time: Manejo de pausas y espera.
"""

from logger.utils.logger_config import logger
from config import USER , PASSWORD
import confirmMessage
import driver_setup
import tasks
import json
import power
import time

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
