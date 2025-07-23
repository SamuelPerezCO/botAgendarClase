from logger.utils.logger_config import logger
from datetime import datetime
import pywhatkit

def sendMessage():
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    ruta_log = f"C:\\Codigos\\botAgendarClase\\src\\logger\\logs\\registro_{fecha_actual}.log"

    with open(ruta_log, "r", encoding="utf-8") as archivo:
        mensaje = archivo.read()

    pywhatkit.sendwhatmsg_instantly("+573167687288", mensaje, wait_time=15, tab_close=True)
    logger.info("Mensaje enviado")


