from modules.utils_config_evaluation import load_data1, save_data1
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
            case 0:
                break
            case _:
                print("❌ Opción inválida")

def register_evaluation():
    data = load_data()
    data1 = load_data1()
    enrollments = data.get("enrollments", [])
    recalibrator = data1.get("recalibrator", [])
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
    for ev in recalibrator:
        if ev["camper_id"] == camper_id and ev["route_nombre"] == enrollment["route_nombre"]:
            print(f"⚠️ El camper {enrollment['camper_nombre']} ya tiene evaluación registrada en {enrollment['route_nombre']}.")
            return

    try:
        nota_teorica = float(input("📝 Ingresa la nota teórica: "))
        nota_w_teorica = float(input("📝 Ingresa la nota w_teórica: "))
        nota_practica = float(input("📝 Ingresa la nota práctica: "))
        nota_w_practica = float(input("📝 Ingresa la nota w_práctica: "))
        nota_asistencia = float(input("📝 Ingresa la nota Asistencia: "))
        nota_w_asistencia = float(input("📝 Ingresa la nota w_asistencia: "))

        if not (0 <= nota_teorica <= 1 and 0 <= nota_practica <= 1):
            print("❌ Las notas deben estar entre 0 y 100.")
            return

        promedio = (nota_teorica * nota_w_teorica + nota_practica * nota_w_practica + nota_asistencia * nota_w_asistencia) / 6
    
        # Definir estado y riesgo
        if promedio >= 1.0:
            estado = "Aprobado"
            riesgo = "Sin riesgo"
        elif promedio >= 0.7:
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

        recalibration = {
            "camper_id": camper_id,
            "camper_nombre": enrollment["camper_nombre"],
            "route_nombre": enrollment["route_nombre"],
            "nota_teorica": nota_teorica,
            "nota_w_teorica": nota_w_teorica,
            "nota_practica": nota_practica,
            "nota_w_practica": nota_practica,
            "nota_asistencia": nota_asistencia,
            "nota_w_asistencia": nota_w_asistencia,
            "promedio": promedio,
            "estado": estado
        }

        recalibrator.append(recalibration)
        save_data1(data1)
        print(f"✅ Evaluación registrada para {enrollment['camper_nombre']} (Promedio: {promedio}, Estado: {estado})")

    except ValueError:
        print("❌ Entrada inválida, debes ingresar números.")
