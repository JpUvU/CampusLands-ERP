from modules.utils import load_data, save_data

def menu():
    while True:
        print("\n--- Gestión de Trainers ---")
        print("1. Registrar trainer")
        print("2. Listar trainers")
        print("3. Buscar trainer por ID")
        print("0. Volver")
        opcion = int(input("Seleccione: "))

        match opcion:
            case 1:
                register_trainer()
            case 2:
                list_trainers()
            case 3:
                search_trainer()
            case 0:
                break
            case _:
                print('❌ Opcion invalida')
                continue

def register_trainer():
    data = load_data()
    
    trainer = {
        "id": int(input("ID del trainer: ")),
        "nombre": input("Nombre: "),
        "apellidos": input("Apellido: "),
        "especialidad": input("Especialidad (NodeJS, Java, NetCore...): "),
        "disponibilidad": input("Disponibilidad (ej: Lunes a Viernes 8am-12pm): ")
    }
    
    data["trainers"].append(trainer)
    save_data(data)
    print("✅ Trainer registrado con éxito.")

def list_trainers():
    data = load_data()
    trainers = data.get("trainers", [])

    if not trainers:
        print("⚠️  No hay trainers registrados.")
        return
    
    print("\n--- Lista de Trainers ---")
    for t in trainers:
        print(f"{t['id']} - {t['nombre']} {t['apellidos']} | Especialidad: {t['especialidad']} | Disponibilidad: {t['disponibilidad']}")

def search_trainer():
    data = load_data()
    trainer = data.get("trainers")
    idTrainerList = []
    try:
        print("\n--- Busca el trainer por id ---")
        idTrainer = int(input('Ingresa el id del trainer: '))
        encontrado = None
        for t in trainer:
            if idTrainer == t['id']:
                encontrado = t
                break
        if encontrado:
            print(f"👨🏻‍🏫 Trainer encontrado: {encontrado['id']} - {encontrado['nombre']} {encontrado['apellidos']} | Especialidad: {encontrado['especialidad']} | Disponibilidad: {encontrado['disponibilidad']}")
        else:
            print('❌ Trainer no encontrado')
    except (ValueError, KeyboardInterrupt):
        print('Dato ingresado es invalido...')