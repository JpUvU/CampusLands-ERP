from modules import campers, trainers, coordinators, routes, enrollments, evaluations, reports, recalibration
import os

def main():
    while True:
        print("\n=== CAMPUSLANDS ERP ===")
        print("1. Gestión de campers")
        print("2. Gestión de trainers")
        print("3. Gestión de coordinadores")
        print("4. Gestión de rutas")
        print("5. Matrículas")
        print("6. Evaluaciones")
        print("7. Reportes")
        print("0. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        
            os.system('cls')
            match opcion:    
                case 1:
                    campers.menu()
                case 2:
                    trainers.menu()
                case 3:
                    coordinators.menu()
                case 4:
                    routes.menu()
                case 5:
                    enrollments.menu()
                case 6:
                    recalibration.menu()
                case 7:
                    reports.menu()         
                case 0:
                    print('Saliste del programa...')
                    break
                case _:
                    print('❌ Opcion invalida')
        except (ValueError, KeyboardInterrupt):
            print('❌ Dato incorrecto, intente nuevamente...')

if __name__ == "__main__":
    main()