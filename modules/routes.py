from modules.utils import load_data, save_data

def menu():
    while True:
        print("\n--- Gestión de Rutas ---")
        print("1. Crear ruta")
        print("2. Listar rutas")
        print("3. Asignar camper aprobado a ruta")
        print("0. Volver")
        try:
            opcion = int(input("Seleccione: "))
        except ValueError:
            print("❌ Ingresa un número válido.")
            continue
        match opcion:
            case 1:
                create_route()
            case 2:
                list_routes()
            case 3:
                assign_camper_to_route()
            case 0:
                print("🚪 Volviendo al menú principal...")
                break
            case _:
                print("❌ Opción inválida.")
                continue

def create_route():
    data = load_data()
    routes = data.get("routes")

    nombre = input("📚 Ingresa el nombre de la ruta: ")
    duracion = input("⏳ Ingresa la duración (ej: 6 meses): ")
    modulos = input("📖 Ingresa los módulos separados por coma: ").split(",")

    nueva_ruta = {
        "id": str(len(routes) + 1),
        "nombre": nombre,
        "duracion": duracion,
        "modulos": modulos,
        "campers_asignados": []
    }

    routes.append(nueva_ruta)
    data["routes"] = routes
    save_data(data)
    print(f"✅ Ruta '{nombre}' creada con éxito.")


def list_routes():
    data = load_data()
    routes = data.get("routes")

    if routes == []:
        print('⚠️ No hay rutas registradas aun...')
    else:
        # Lista todas las rutas registradas.
        print("\n📚 Listado de Rutas:")
        for r in routes:
            print(f"{r['id']} - {r['nombre']} ({r['duracion']})")
            print(f"   Módulos: {(r['modulos'])}")
            print(f"   Campers asignados: {len(r['campers_asignados'])}")
            print("-" * 40)

def assign_camper_to_route():
    data = load_data()
    campers = data.get("campers")
    routes = data.get("routes")
    aprobados = []

    # Listar campers aprobados
    for c in campers:
        if c['estado'] == 'Aprobado':
            print(f"{c['id']} - {c['nombre']} {c['apellidos']}")
            aprobados.append(c['nombre'])

    # Validación de campers aprobados
    if aprobados == []:
        print('⚠️ No hay ningun registro de campers aprobados para asignar...')
        return

    # Validación de rutas
    if routes == []:
        print("⚠️ No hay rutas disponibles. Primero crea una ruta.")
        return

    camper_id = int(input("👉 Ingresa el ID del camper a asignar: "))

    for c in campers:
        # Verifica que el id ingresado corresponda y de paso que tambien corresponda el estado en "Aprobado"
        if c['id'] == camper_id and c['estado'] == 'Aprobado':
            print(f'Deseas asignar a {c["id"]} - {c["nombre"]} - {c["apellidos"]} ')
            asignar = input('Ingrese "S" para si y "N" para no...: ').strip().upper()

            if asignar == 'S':
                print("\n📚 Rutas disponibles:")
                for r in routes:
                    print(f"{r['id']} - {r['nombre']}")

                route_id = input("👉 Ingresa el ID de la ruta a asignar: ")

                # Recorremos las rutas para encontrar la seleccionada
                for r in routes:
                    if r['id'] == route_id:  # comparo string con string
                        if camper_id not in r['campers_asignados']:  # comparo int con lista de int
                            r["campers_asignados"].append(camper_id)
                            save_data(data)
                            print(f"✅ Camper {c['nombre']} asignado a la ruta {r['nombre']}.")
                        else:
                            print('❌ Lo sentimos, el camper ya hace parte de esta ruta...')
                        return
                print("❌ Ruta no encontrada.")
            else:
                print('❌ No asignaras nada.')
            return

    # Si no encuentra camper aprobado con ese ID
    print("❌ Camper no encontrado o no está aprobado.")
