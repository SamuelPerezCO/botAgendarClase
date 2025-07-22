from logger.utils.logger_config import logger
from config import USER , PASSWORD
import driver_setup
import tasks
import json

driver = driver_setup.setup()

# Leer desde el archivo y enviar los datos
with open("clases.txt", "r") as archivo:
    clases_leidas = json.load(archivo)

logger.info("-" * 25 + "INICIO" + "-" * 25)

tasks.login(USER ,PASSWORD ,driver)
tasks.closePopUpAndClickOnSchedule(driver)
tasks.classList(driver)
#Le tengo que enviar la clase

for numero_clase , detalles in clases_leidas.items():
    tasks.scheduleClass(driver , numero_clase)
    tasks.scheduleBranchDayTime(driver, detalles["sede"] , detalles["dia"] , detalles["hora"])


tasks.outOfWebPage(driver)

logger.info("-" * 25 + "FIN" + "-" * 25)

# if __name__ == "__main__":
#     main()