"""Script para registrar y guardar clases en un archivo JSON.

Este script:
    1. Solicita al usuario el número de clases a registrar.
    2. Pide los datos de cada clase:
        - Nombre o número de la clase.
        - Sede.
        - Día.
        - Hora (en formato XPath).
    3. Guarda toda la información en un archivo `clases.txt` en formato JSON.

Uso:
    Ejecutar el script y seguir las instrucciones en consola.
"""
import json

clases = {}
cantidad = int(input("Numero de clases: "))

# Registro y guardado
for i in range(cantidad):
    numero_clase = input(f"Ingrese Clase (Texto) {i+1} (EJ: CLASE 19): ")
    sede = input(f"Sede (Texto) {numero_clase} (EJ:ENVIGADO): ")
    dia = input(f"Dia (Texto) {numero_clase} (EJ:LUNES DIA/MES/AÑO): ")
    hora = input(f"Hora (XPATH) {numero_clase} (EJ://*[@id=\\\"Grid1ContainerRow_0010\\\"]): ")
    
    clases[numero_clase] = {
        "sede": sede,
        "dia": dia,
        "hora": hora
    }

with open("clases.txt", "w") as archivo:
    json.dump(clases, archivo)
