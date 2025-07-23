import json

clases = {}
cantidad = int(input("Numero de clases: "))

# Registro y guardado
for i in range(cantidad):
    numero_clase = input(f"Ingrese Clase: {i+1}: ")
    sede = input(f"Sede (Texto) EJ: ENVIGADO {numero_clase}: ")
    dia = input(f"Dia (Texto) EJ: LUNES DIA/MES/AÑO{numero_clase}: ")
    hora = input(f"Hora (XPATH) EJ: //*[@id=\\\"Grid1ContainerRow_0010\\\"] {numero_clase}: ")
    
    clases[numero_clase] = {
        "sede": sede,
        "dia": dia,
        "hora": hora
    }

with open("clases.txt", "w") as archivo:
    json.dump(clases, archivo)
