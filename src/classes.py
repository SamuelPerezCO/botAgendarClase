import json

clases = {}
cantidad = int(input("Numero de clases: "))

# Registro y guardado
for i in range(cantidad):
    numero_clase = input(f"Ingrese el numero_clase de la clase {i+1}: ")
    sede = input(f"Sede (Texto) {numero_clase}: ")
    dia = input(f"Dia (Texto) {numero_clase}: ")
    hora = input(f"Hora (XPATH) {numero_clase}: ")
    
    clases[numero_clase] = {
        "sede": sede,
        "dia": dia,
        "hora": hora
    }

with open("clases.txt", "w") as archivo:
    json.dump(clases, archivo)
