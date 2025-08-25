from modules.utils import load_data, save_data

def menu():
    while True:
        print("\n--- Gestión de Matrículas ---")
        print("1. Crear matrícula")
        print("2. Listar matrículas")
        print("0. Volver")
        try:
            opcion = int(input("Seleccione: "))
        except ValueError:
            print("❌ Ingresa un número válido.")
            continue

        match opcion:
            case 1:
                create_enrollment()
            case 2:
                list_enrollments()
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

    disponibles = []

    # Listar campers aprobados con ruta asignada
    print("\n👨‍🎓 Campers aprobados con ruta asignada:")
    for c in campers:
        for r in routes:       
            if c["estado"] == "Aprobado" and c['id'] in r['campers_asignados']:
            # verificar si ya está matriculado
                existe = False
                for e in enrollments:
                    if e['camper_id'] == c['id']:
                        existe = True
                        break
            
                if not existe:  # solo mostrar si NO tiene matrícula
                    print(f"{c['id']} - {c['nombre']} {c['apellidos']} (Ruta: {r['nombre']})")
                    disponibles.append(c)

    if disponibles == []:
        print("⚠️ No hay campers aprobados con ruta asignada para matricular.")
        return

    # Validación de rutas
    if routes == []:
        print("⚠️ No hay rutas disponibles.")
        return

    # Validación de trainers
    if trainers == []:
        print("⚠️ No hay trainers registrados.")
        return

    camper_id = int(input("👉 Ingresa el ID del camper a matricular: "))

    for c in campers:
        for r in routes:
            if c['id'] == camper_id and camper_id in r['campers_asignados']:

                # Verificar si ya está matriculado
                for e in enrollments:
                    if e["camper_id"] == camper_id and e["route_nombre"] == r["nombre"]:
                        print(f"⚠️ El camper {c['nombre']} ya está matriculado en la ruta {r['nombre']}.")
                        return

                # Crear lista de trainers ya ocupados
                trainers_ocupados = [e["trainer_id"] for e in enrollments]

                # Mostrar solo trainers disponibles
                print("\n👨‍🏫 Trainers disponibles:")
                for t in trainers:
                    if t['id'] not in trainers_ocupados:
                        print(f"{t['id']} - {t['nombre']} {t['apellidos']} (Especialidad: {t['especialidad']})")

                # Pedir trainer
                trainer_id = int(input("👉 Ingresa el ID del trainer: "))

                # Verificar trainer
                trainer_seleccionado = None
                for t in trainers:
                    if t['id'] == trainer_id:
                        if t['id'] in trainers_ocupados:
                            print(f"⚠️ El trainer {t['nombre']} {t['apellidos']} ya está asignado.")
                            return
                        else:
                            trainer_seleccionado = t
                            break

                if not trainer_seleccionado:
                    print("❌ Trainer no encontrado.")
                    return

                # Asignar salón (simple input)
                salon = input("🏫 Ingresa el salón asignado: ")

                # Crear matrícula
                enrollment = {
                    "camper_id": camper_id,
                    "camper_nombre": c["nombre"],
                    "route_nombre": r["nombre"],
                    "trainer_id": trainer_seleccionado["id"],
                    "trainer_nombre": trainer_seleccionado["nombre"],
                    "salon": salon
                }
                enrollments.append(enrollment)
                save_data(data)
                print(f"✅ Camper {c['nombre']} matriculado en {r['nombre']} con el trainer {trainer_seleccionado['nombre']} en el salón {salon}")
                return

    print("❌ Camper no encontrado o no tiene ruta asignada.")



def list_enrollments():
    data = load_data()
    enrollments = data.get("enrollments", [])
    routes = data.get("routes", [])

    if not enrollments:
        print("⚠️ No hay matrículas registradas aún.")
        return

    print("\n--- Lista de Matrículas por Ruta ---")

    # Agrupar campers por ruta
    rutas = {}
    for e in enrollments:
        ruta = e["route_nombre"]
        if ruta not in rutas:
            rutas[ruta] = []
        rutas[ruta].append(e)

    # Imprimir agrupado con detalles de cada ruta
    for ruta, lista in rutas.items():
        # Buscar detalles de la ruta en data["routes"]
        detalles = next((r for r in routes if r["nombre"] == ruta), None)

        if detalles:
            print(f"\n📚 Ruta: {detalles['nombre']} | Duración: {detalles['duracion']}")
            print("   📘 Módulos:", ", ".join(detalles["modulos"]))
        else:
            print(f"\n📚 Ruta: {ruta}")

        # Imprimir campers de la ruta
        for e in lista:
            print(f"   👨‍🎓 Camper: {e['camper_nombre']} | Trainer: {e.get('trainer_nombre', 'No asignado')} | Salón: {e.get('salon', 'No asignado')}")
