from modules.utils import load_data

def menu():
    while True:
        print("\n--- Gestión de Reportes ---")
        print("1. Listar campers inscritos")
        print("2. Listar campers aprobados en examen inicial")
        print("3. Listar trainers de CampusLands")
        print("4. Listar campers con bajo rendimiento")
        print("5. Listar campers y trainers asociados a rutas")
        print("6. Reporte de aprobados y reprobados por módulo")
        print("0. Volver")
        
        opcion = input("Seleccione: ")

        match opcion:
            case "1":
                list_campers_inscritos()
            case "2":
                list_campers_aprobados()
            case "3":
                list_trainers()
            case "4":
                list_campers_bajo_rendimiento()
            case "5":
                list_campers_trainers_rutas()
            case "6":
                report_aprobados_reprobados()
            case "0":
                break
            case _:
                print("❌ Opción inválida")


# 1. Listar campers en estado de inscrito
def list_campers_inscritos():
    data = load_data()
    campers = data.get("campers", [])

    print("\n👦 Campers inscritos:")
    encontrados = [c for c in campers if c["estado"] == "En proceso de ingreso"]

    if not encontrados:
        print("⚠️ No hay campers inscritos actualmente.")
        return

    for c in encontrados:
        print(f"{c['id']} - {c['nombre']} {c['apellidos']} ({c['estado']})")


# 2. Listar campers aprobados en examen inicial
def list_campers_aprobados():
    data = load_data()
    campers = data.get("campers", [])

    print("\n✅ Campers aprobados:")
    aprobados = [c for c in campers if c["estado"] == "Aprobado"]

    if not aprobados:
        print("⚠️ No hay campers aprobados aún.")
        return

    for c in aprobados:
        print(f"{c['id']} - {c['nombre']} {c['apellidos']} ({c['estado']})")


# 3. Listar trainers registrados
def list_trainers():
    data = load_data()
    trainers = data.get("trainers", [])

    print("\n👨‍🏫 Trainers de CampusLands:")
    if not trainers:
        print("⚠️ No hay trainers registrados.")
        return

    for t in trainers:
        print(f"{t['id']} - {t['nombre']} {t['apellidos']} | Especialidad: {t['especialidad']}")


# 4. Listar campers con bajo rendimiento (según riesgo)
def list_campers_bajo_rendimiento():
    data = load_data()
    campers = data.get("campers", [])

    print("\n📉 Campers con bajo rendimiento:")
    bajos = [c for c in campers if c["Riesgo"] in ["Medio", "Alto"]]

    if not bajos:
        print("⚠️ No hay campers con bajo rendimiento.")
        return

    for c in bajos:
        print(f"{c['id']} - {c['nombre']} {c['apellidos']} (Riesgo: {c['Riesgo']})")


# 5. Listar campers y trainers asociados a rutas
def list_campers_trainers_rutas():
    data = load_data()
    routes = data.get("routes", [])
    enrollments = data.get("enrollments", [])

    print("\n📚 Campers y Trainers asociados a rutas:")
    if not enrollments:
        print("⚠️ No hay matrículas registradas.")
        return

    for r in routes:
        print(f"\n🔹 Ruta: {r['nombre']}")
        for e in enrollments:
            if e["route_nombre"] == r["nombre"]:
                print(f"   👦 Camper: {e['camper_nombre']} | 👨‍🏫 Trainer: {e.get('trainer_nombre','No asignado')}")


# 6. Reporte de aprobados y reprobados por módulo
def report_aprobados_reprobados():
    data = load_data()
    evaluations = data.get("evaluations", [])
    routes = data.get("routes", [])

    print("\n📊 Reporte de aprobados/reprobados por módulo:")
    if not evaluations:
        print("⚠️ No hay evaluaciones registradas.")
        return

    for r in routes:
        print(f"\n🔹 Ruta: {r['nombre']}")
        modulos = r["modulos"]
        for m in modulos:
            aprobados = 0
            reprobados = 0
            for e in evaluations:
                if e["route_nombre"] == r["nombre"]:
                    if e["promedio"] >= 60:
                        aprobados += 1
                    else:
                        reprobados += 1
            print(f"   📘 Módulo: {m} | ✅ Aprobados: {aprobados} | ❌ Reprobados: {reprobados}")
