from datetime import datetime
import pywhatkit

fecha_actual = datetime.now().strftime("%Y-%m-%d")
ruta_log = f"C:\\Codigos\\botAgendarClase\\src\\logger\\logs\\registro_{fecha_actual}.log"


# Leer el contenido del archivo txt
with open("mensaje.txt", "r", encoding="utf-8") as archivo:
    mensaje = archivo.read()

# Enviar mensaje por WhatsApp
# Sintaxis: pywhatkit.sendwhatmsg("número", "mensaje", hora, minuto)
pywhatkit.sendwhatmsg("+573234920950", mensaje)  # Cambia por tu número y hora
