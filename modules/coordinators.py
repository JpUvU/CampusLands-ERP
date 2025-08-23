from modules.utils import load_data, save_data

def menu():
    while True:
        print("\n--- Gestión de Coordinadores ---")
        print("1. Evaluar camper (prueba inicial)")
        print("2. Listar campers en proceso de ingreso")
        print("0. Volver")
        opcion = int(input("Seleccione: "))

        match opcion:
            case 1:
                evaluate_camper()
            case 2:
                list_campers_process_admission()
            case 0:
                print('🚪 Has salido al menu principal')
                break
            case _:
                print('❌ Opcion invalida')

def evaluate_camper():
    data = load_data()
    camper = data.get("campers")

    for c in camper:
        if c["estado"] == 'En proceso de ingreso':
            print(f"{c['id']} - {c['nombre']} {c['apellidos']} ({c['estado']})")

    seleccion_camper = int(input('Selecciona el camper por su id, para evaluar: '))
    for c in camper:
        if c["id"] == seleccion_camper and c["estado"] != "Aprobado":
            print('Camper seleccionado: ⬇️')
            print(f"{c['id']} - {c['nombre']} {c['apellidos']} ({c['estado']})")
            try:
                print('El rango de la nota al ingresa debe ser del 1 al 100')
                nota_teorica = float(input(f'🗒️ Ingresa la nota teorica de {c["nombre"]}: '))
                nota_practica = float(input(f'📝 Ingresa la nota teorica de {c["nombre"]}: '))
                if nota_teorica < 0 or nota_teorica > 100 or nota_practica < 0 or nota_practica > 100:
                    print('❌ El rango ingresado es invalido... ')
                else:
                    promedio = (nota_teorica + nota_practica) / 2
                    # Actualizar estado según promedio
                    if promedio >= 60:
                        c["estado"] = "Aprobado"
                        print(f"✅ {c['nombre']} {c['apellidos']} ha sido APROBADO (Promedio: {promedio}).")
                    else:
                        c["estado"] = "Rechazado"
                        print(f"❌ {c['nombre']} {c['apellidos']} ha sido RECHAZADO (Promedio: {promedio}).")
                    save_data(data)                
            except (ValueError):
                print('Dato ingresado es invalido...')
            return
        if c["id"] == seleccion_camper and c["estado"] == "Aprobado":
            print('👦🏻 Este camper ya fue aprobado')
            return
            
def list_campers_process_admission():
    data = load_data()
    camper_process = data.get("campers")
    campers = []

    # Encuentra los estudiantes en proceso de ingreso
    for c in camper_process:       
        if c["estado"] == 'En proceso de ingreso':
            print('➡️ Listado de campers en proceso de ingreso: \n ')
            lista = (f"{c['id']} - {c['nombre']} {c['apellidos']} ({c['estado']})")
            campers.append(lista)
            print(lista)
    # Nos dice si no hay ningun estudiante en proceso
    if campers == []:
        print('⚠️ No hay estudiantes en proceso de ingreso...')