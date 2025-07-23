import json

clases = {}
cantidad = int(input("Numero de clases: "))

# Registro y guardado
for i in range(cantidad):
    numero_clase = input(f"Ingrese Clase: {i+1}: ")
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
