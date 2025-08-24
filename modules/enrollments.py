from modules.utils import load_data, save_data

def menu():
    while True:
        print("\n--- Gestión de Matrículas ---")
        print("1. Crear matrícula")
        print("2. Listar matrículas")
        print("0. Volver")
        try:
            opcion = int(input("Seleccione: "))
        except (ValueError, KeyboardInterrupt):
            print("❌ Ingresa un número válido.")
            continue

        match opcion:
            case 1:
                #create_enrollment()
                pass
            case 2:
                #list_enrollments()
                pass
            case 0:
                print("🚪 Volviendo al menú principal...")
                break
            case _:
                print("❌ Opción inválida.")


def create_enrollment():
    data = load_data()
    campers = data.get("campers")
    routes = data.get("routes")
    trainers = data.get("trainers")
    enrollments = data.get("enrollments")

    # 1: Listar campers ya asignados en una ruta.

    pass

