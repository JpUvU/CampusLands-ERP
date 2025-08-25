from modules.utils import load_data, save_data

def menu():
    while True:
        print("\n--- Gestión de Evaluaciones ---")
        print("1. Registrar evaluación")
        print("2. Listar evaluaciones")
        print("0. Volver")

        try:
            opcion = int(input("Seleccione: "))
        except (ValueError, KeyboardInterrupt):
            print('❌ Dato invalido...')

        match opcion:
            case 1:
                register_evaluation()
            case 2:
                list_evaluations()
            case 0:
                break
            case _:
                print("❌ Opción inválida")

def register_evaluation():
    data = load_data()
    enrollments = data.get("enrollments", [])
    evaluations = data.get("evaluations", [])
    campers = data.get('campers')

    if not enrollments:
        print("⚠️ No hay matrículas registradas, no puedes evaluar.")
        return

    print("\n👨‍🎓 Campers matriculados:")
    for e in enrollments:
        print(f"{e['camper_id']} - {e['camper_nombre']} (Ruta: {e['route_nombre']})")

    camper_id = int(input("👉 Ingresa el ID del camper a evaluar: "))

    # Buscar matrícula
    enrollment = None
    for e in enrollments:
        if e["camper_id"] == camper_id:
            enrollment = e
            break

    if not enrollment:
        print("❌ El camper no está matriculado.")
        return

    # Verificar si ya tiene evaluación
    for ev in evaluations:
        if ev["camper_id"] == camper_id and ev["route_nombre"] == enrollment["route_nombre"]:
            print(f"⚠️ El camper {enrollment['camper_nombre']} ya tiene evaluación registrada en {enrollment['route_nombre']}.")
            return

    try:
        nota_teorica = float(input("📝 Ingresa la nota teórica: "))
        nota_practica = float(input("📝 Ingresa la nota práctica: "))

        if not (0 <= nota_teorica <= 100 and 0 <= nota_practica <= 100):
            print("❌ Las notas deben estar entre 0 y 100.")
            return

        promedio = (nota_teorica + nota_practica) / 2
    
        # Definir estado y riesgo
        if promedio >= 60:
            estado = "Aprobado"
            riesgo = "Sin riesgo"
        elif promedio >= 40:
            estado = "En riesgo"
            riesgo = "Medio"
        else:
            estado = "En riesgo"
            riesgo = "Alto"

        # Actualizar camper en la base de datos
        for c in campers:
            if c["id"] == camper_id:
                c["Riesgo"] = riesgo
                break

        evaluation = {
            "camper_id": camper_id,
            "camper_nombre": enrollment["camper_nombre"],
            "route_nombre": enrollment["route_nombre"],
            "nota_teorica": nota_teorica,
            "nota_practica": nota_practica,
            "promedio": promedio,
            "estado": estado
        }

        evaluations.append(evaluation)
        save_data(data)
        print(f"✅ Evaluación registrada para {enrollment['camper_nombre']} (Promedio: {promedio}, Estado: {estado})")

    except ValueError:
        print("❌ Entrada inválida, debes ingresar números.")

def list_evaluations():
    data = load_data()
    evaluations = data.get("evaluations", [])

    if not evaluations:
        print("⚠️ No hay evaluaciones registradas aún.")
        return

    # Agrupar evaluaciones por ruta
    evaluaciones_por_ruta = {}
    for ev in evaluations:
        ruta = ev["route_nombre"]
        if ruta not in evaluaciones_por_ruta:
            evaluaciones_por_ruta[ruta] = []
        evaluaciones_por_ruta[ruta].append(ev)

    # Mostrar evaluaciones agrupadas
    for ruta, lista in evaluaciones_por_ruta.items():
        print(f"\n📚 Ruta: {ruta}")
        print("-" * 40)
        for ev in lista:
            print(f"👨‍🎓 {ev['camper_id']} - {ev['camper_nombre']} | "
                  f"Teórica: {ev['nota_teorica']} | "
                  f"Práctica: {ev['nota_practica']} | "
                  f"Promedio: {ev['promedio']} | "
                  f"Estado: {ev['estado']}")

