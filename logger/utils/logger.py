import logging
from datetime import datetime

def _set_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(filename)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Nombre de archivo con la fecha
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    ruta_log = f"C:\\Codigos\\botAgendarClase\\logger\\logs\\registro_{fecha_actual}.log"

    file_handler = logging.FileHandler(ruta_log, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

if __name__ == "__main__":
    _set_logger()

    logging.debug("Mensaje debug")
    logging.info("Mensaje info")
    logging.warning("Mensaje warning")
    logging.error("Mensaje error")
    logging.critical("Mensaje crítico")
