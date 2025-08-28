import json

ARCHIVO_BASE_DATOS = "/CampusLands-ERP/data/config_evaluacion.json"

# Carga la informacion
def load_data1():
    try:
        with open(ARCHIVO_BASE_DATOS, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Guarda la informacion
def save_data1(data):
    with open(ARCHIVO_BASE_DATOS, "w") as f:
        json.dump(data, f, indent=4)
