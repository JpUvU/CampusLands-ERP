from modules.utils import load_data, save_data

def menu():
    while True:
        print("\n--- Gestión de Campers ---")
        print("1. Registrar camper")
        print("2. Listar campers")
        print("0. Volver")
        opcion = int(input("Seleccione: "))

        match opcion:
            case 1:
                register_camper()
            case 2:
                list_campers()
            case 0:
                break
            case _:
                print('Opcion invalida')

def register_camper():
    data = load_data()
    camper = {
        "id": int(input("ID: ")),
        "nombre": input("Nombre: "),
        "apellidos": input("Apellido: "),
        "direccion": input("Direccion: "),
        "Telefono": int(input('Telefono de contacto: ')),
        "estado": "En proceso de ingreso",
        "Riesgo": "Sin riesgo"
    }
    data["campers"].append(camper)
    save_data(data)
    print("✅ Camper registrado.")

def list_campers():
    data = load_data()
    for c in data["campers"]:
        print(f"{c['id']} - {c['nombre']} {c['apellidos']} ({c['estado']})")