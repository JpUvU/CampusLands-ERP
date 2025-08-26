🗃️ CampusLands-ERP

El departamento académico de CampusLands desea llevar el seguimiento académico de todos los campers que se encuentran matriculados en el programa intensivo de programación.

Este sistema permite gestionar campers, trainers, rutas de entrenamiento, matrículas, evaluaciones y reportes, con persistencia de datos en formato JSON.

---------------------------------------------------------------------------------------------------------------------------
🛠️ Stack Tecnológico

🐍 Python

➰ Bucles

📚 Diccionarios

🤼 Condicionales

📂 Módulos

---------------------------------------------------------------------------------------------------------------------------

📂 Estructura del Proyecto

CampusLands-ERP/
│── data/
│   └── database.json        # Base de datos en formato JSON
│
│── modules/                 # Carpeta de módulos con la lógica del sistema
│   ├── campers.py
│   ├── trainers.py
│   ├── coordinators.py
│   ├── routes.py
│   ├── enrollments.py
│   ├── evaluations.py
│   └── reports.py
|   └── utils.py            # Funciones auxiliares (persistencia)
│
│                  
│   
│
│── main.py                  # Punto de entrada principal del programa
│── README.md


---------------------------------------------------------------------------------------------------------------------------

📖 Librerías Utilizadas:

🐻 os → Para ejecutar comandos del sistema y limpiar la terminal

🗃️ json → Para manejar la persistencia de datos en formato JSON

---------------------------------------------------------------------------------------------------------------------------
🚀 Ejecución:

Clonar o descargar el proyecto en tu equipo.

Abrir una terminal en la carpeta del proyecto.

Ejecutar el programa con:

🐍 python main.py

---------------------------------------------------------------------------------------------------------------------------

⚠️ Nota Importante sobre la Ruta de Datos:

Por defecto, el sistema busca la base de datos en:

ARCHIVO_BASE_DATOS = "data/database.json"

⚠️  Si tu proyecto está dentro de otra carpeta, debes ajustar la ruta:
    
Por ejemplo:

ARCHIVO_BASE_DATOS = "CAMPUSLANDS-ERP/data/database.json"

---------------------------------------------------------------------------------------------------------------------------

📌 Requerimientos

Compatible con Linux y Windows

Tener instalada una versión de Python 3.8 o superior

---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------
🎯 Funcionalidades del Sistema

✅ Gestión de campers
✅ Gestión de trainers y coordinadores
✅ Registro y administración de rutas de entrenamiento
✅ Matrículas
✅ Evaluaciones académicas
✅ Reportes y consultas personalizadas
