import json

clases = {}
cantidad = int(input("¿Cuántas clases quieres ingresar?: "))

def imprimo_la_clase(numero_clase):
    print(f"Clase: {numero_clase}")

def imprimo_la_sede(sede):
    print(f"Sede: {sede}")

def imprimo_la_hora(hora):
    print(f"Hora: {hora}")

# Registro y guardado
for i in range(cantidad):
    numero_clase = input(f"Ingrese el numero_clase de la clase {i+1}: ")
    sede = input(f"Ingrese el sede para {numero_clase}: ")
    dia = input(f"Ingrese el dia para {numero_clase}: ")
    hora = input(f"Ingrese la hora para {numero_clase}: ")
    
    clases[numero_clase] = {
        "sede": sede,
        "dia": dia,
        "hora": hora
    }

# # Guardar en archivo
# with open("clases.txt", "w") as archivo:
#     json.dump(clases, archivo)

# print("\nClases guardadas correctamente\n")

# # Leer desde el archivo y enviar los datos
# with open("clases.txt", "r") as archivo:
#     clases_leidas = json.load(archivo)

# print("Clases leídas desde el archivo:\n")

# for numero_clase, detalles in clases_leidas.items():
#     imprimo_la_clase(numero_clase)
#     imprimo_la_sede(detalles["sede"])
#     imprimo_la_hora(detalles["hora"])
