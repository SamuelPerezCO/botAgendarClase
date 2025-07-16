import logging
from datetime import datetime

fecha_actual = datetime.now().strftime("%Y-%m-%d")
ruta_log = f"C:\\Codigos\\botAgendarClase\\src\\logger\\logs\\registro_{fecha_actual}.log"

formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(filename)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("mi_logger")
logger.setLevel(logging.DEBUG)

# Evitar handlers duplicados si se llama varias veces
if not logger.hasHandlers():
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(ruta_log, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
