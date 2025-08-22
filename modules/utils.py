import json

ARCHIVO_BASE_DATOS = "data/database.json"

# Carga la informacion
def load_data():
    try:
        with open(ARCHIVO_BASE_DATOS, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Guarda la informacion
def save_data(data):
    with open(ARCHIVO_BASE_DATOS, "w") as f:
        json.dump(data, f, indent=4)
