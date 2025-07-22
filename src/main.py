from logger.utils.logger_config import logger
from config import USER , PASSWORD
import driver_setup
import tasks
import json

driver = driver_setup.setup()

# Leer desde el archivo y enviar los datos
with open("clases.txt", "r") as archivo:
    clases_leidas = json.load(archivo)

print("Clases leídas desde el archivo:\n")

for numero_clase, detalles in clases_leidas.items():
    print(f"Numero de clase : {numero_clase}")
    print(f"Sede: {detalles["sede"]}")
    print(f"Dia: {detalles["dia"]}")
    print(f"Hora: {detalles["hora"]}")
    print("--------------------------")

logger.info("-" * 25 + "INICIO" + "-" * 25)

tasks.login(USER ,PASSWORD ,driver)
tasks.closePopUpAndClickOnSchedule(driver)
tasks.classList(driver)
#Le tengo que enviar la clase
tasks.scheduleClass(driver)
tasks.scheduleBranchDayTime(driver)

tasks.outOfWebPage(driver)

logger.info("-" * 25 + "FIN" + "-" * 25)

# if __name__ == "__main__":
#     main()