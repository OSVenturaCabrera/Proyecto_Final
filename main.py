# ============================== Usted esta en Curso.
# SISTEMA ESCOLAR BÁSICO
# ==============================
<<<<<<< HEAD
import json
import os

import os
os.system("cls") # limpiar consola
=======
import os
os.system("cls")
>>>>>>> f2bad45238d7151b5463c04ec3533d9c1d2d693a

# Diccionarios para almacenar la información
estudiantes = {}
maestros = {}
cursos = {}
notas = {}

# ------------------------------
# Funciones de gestión de estudiantes
# ------------------------------
def agregar_estudiante(nombre, id_estudiante):
    """Agrega un estudiante al sistema"""
    estudiantes[id_estudiante] = nombre
    print(f"Estudiante {nombre} agregado con ID {id_estudiante}.")

def eliminar_estudiante(id_estudiante):
    """Elimina un estudiante del sistema"""
    if id_estudiante in estudiantes:
        del estudiantes[id_estudiante]
        print(f"Estudiante con ID {id_estudiante} eliminado.")
    else:
        print("Estudiante no encontrado.")

def listar_estudiantes():
    """Muestra todos los estudiantes"""
    print("Lista de estudiantes:")
    for id_est, nombre in estudiantes.items():
        print(f"ID: {id_est}, Nombre: {nombre}")

def buscar_estudiante(id_estudiante):
    """Busca un estudiante por ID"""
    nombre = estudiantes.get(id_estudiante)
    if id_estudiante in estudiantes.keys():
        print(f"el estudiante del ID: {id_estudiante} es {nombre}")
    else:
        print("Error!!, ID no encontrado.")

# ------------------------------
# Funciones de gestión de maestros
# ------------------------------
def agregar_maestro(nombre, id_maestro):
    """Agrega un maestro al sistema"""
    maestros[id_maestro] = nombre
    print(f"Maestro {nombre} agregado con ID {id_maestro}.")

def eliminar_maestro(id_maestro):
    """Elimina un maestro del sistema"""
    if id_maestro in maestros:
        del maestros[id_maestro]
        print(f"Maestro con ID {id_maestro} eliminado.")
    else:
        print("Maestro no encontrado.")

def listar_maestros():
    """Muestra todos los maestros"""
    print("Lista de maestros:")
    for id_m, nombre in maestros.items():
        print(f"ID: {id_m}, Nombre: {nombre}")

def buscar_maestro(id_maestro):
    """Busca un maestro por ID"""
    return maestros.get(id_maestro, "Maestro no encontrado")

# ------------------------------
# Funciones de gestión de cursos
# ------------------------------
def agregar_curso(nombre_curso, id_curso):
    """Agrega un curso al sistema"""
    cursos[id_curso] = {"nombre": nombre_curso, "maestro": None}
    print(f"Curso {nombre_curso} agregado con ID {id_curso}.")

def eliminar_curso(id_curso):
    """Elimina un curso del sistema"""
    if id_curso in cursos:
        del cursos[id_curso]
        print(f"Curso con ID {id_curso} eliminado.")
    else:
        print("Curso no encontrado.")

def listar_cursos():
    """Muestra todos los cursos"""
    print("Lista de cursos:")
    for id_c, info in cursos.items():
        maestro = info["maestro"] or "Sin asignar"
        print(f"ID: {id_c}, Nombre: {info['nombre']}, Maestro: {maestro}")

def asignar_maestro_curso(id_maestro, id_curso):
    """Asocia un maestro a un curso"""
    if id_curso in cursos and id_maestro in maestros:
        cursos[id_curso]["maestro"] = maestros[id_maestro]
        print(f"Maestro {maestros[id_maestro]} asignado al curso {cursos[id_curso]['nombre']}.")
    else:
        print("Curso o maestro no encontrado.")

# ------------------------------
# Funciones de notas
# ------------------------------
def agregar_nota(id_estudiante, id_curso, nota):
    """Agrega una nota para un estudiante en un curso"""
    if id_estudiante not in estudiantes or id_curso not in cursos:
        print("Estudiante o curso no encontrado.")
        return
    notas.setdefault(id_curso, {})
    notas[id_curso].setdefault(id_estudiante, [])
    notas[id_curso][id_estudiante].append(nota)
    print(f"Nota {nota} agregada para {estudiantes[id_estudiante]} en {cursos[id_curso]['nombre']}.")

def listar_notas_estudiante(id_estudiante):
    """Muestra todas las notas de un estudiante"""
    print(f"Notas de {estudiantes.get(id_estudiante, 'Estudiante no encontrado')}:")
    for id_c, estudiantes_curso in notas.items():
        if id_estudiante in estudiantes_curso:
            print(f"{cursos[id_c]['nombre']}: {estudiantes_curso[id_estudiante]}")

def calcular_promedio(id_estudiante):
    """Calcula el promedio de todas las notas de un estudiante"""
    total = 0
    count = 0
    for estudiantes_curso in notas.values():
        if id_estudiante in estudiantes_curso:
            total += sum(estudiantes_curso[id_estudiante])
            count += len(estudiantes_curso[id_estudiante])
    if count == 0:
        return None
    return total / count

def mejores_estudiantes(id_curso, n=5):
    """Devuelve los mejores estudiantes de un curso"""
    if id_curso not in notas:
        print("No hay notas registradas para este curso.")
        return
    promedio_estudiantes = {}
    for id_est, lista_notas in notas[id_curso].items():
        promedio_estudiantes[id_est] = sum(lista_notas) / len(lista_notas)
    mejores = sorted(promedio_estudiantes.items(), key=lambda x: x[1], reverse=True)[:n]
    print(f"Mejores estudiantes del curso {cursos[id_curso]['nombre']}:")
    for id_est, prom in mejores:
        print(f"{estudiantes[id_est]} - Promedio: {prom:.2f}")

# ------------------------------
# Funciones de utilidad
# ------------------------------
def guardar_datos():
    """Guarda los datos en archivos JSON"""
    with open("estudiantes.json", "w", encoding="utf-8") as f:
        json.dump(estudiantes, f)
    with open("maestros.json", "w", encoding="utf-8") as f:
        json.dump(maestros, f)
    with open("cursos.json", "w", encoding="utf-8") as f:
        json.dump(cursos, f)
    with open("notas.json", "w", encoding="utf-8") as f:
        json.dump(notas, f)
    print("Datos guardados correctamente.")

def cargar_datos():
    """Carga los datos desde archivos JSON si existen"""
    global estudiantes, maestros, cursos, notas
    if os.path.exists("estudiantes.json"):
        with open("estudiantes.json", "r", encoding="utf-8") as f:
            estudiantes = json.load(f)
    if os.path.exists("maestros.json"):
        with open("maestros.json", "r", encoding="utf-8") as f:
            maestros = json.load(f)
    if os.path.exists("cursos.json"):
        with open("cursos.json", "r", encoding="utf-8") as f:
            cursos = json.load(f)
    if os.path.exists("notas.json"):
        with open("notas.json", "r", encoding="utf-8") as f:
            notas = json.load(f)
    print("Datos cargados correctamente.")
# ------------------------------
# Menú principal
# ------------------------------
def menu_principal():
    while True:
        print("\n--- SISTEMA ESCOLAR ---")
        print("1. Gestionar Estudiantes")
        print("2. Gestionar Maestros")
        print("3. Gestionar Cursos")
        print("4. Gestionar Notas")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
<<<<<<< HEAD
            print("Opciones de estudiantes, presione el numero segun su opcion: ")
            op = int(input("\n1: agregar, 2: eliminar, 3: listar, 4: buscar | "))
            match op:
                case 1:
                    cantidad = int(input("Cuantos estudiantes desea ingresar? "))
                    try:
                        for i in range(cantidad):
                            nombre_estudiante = str(input("Ingresa el nombre de tu estudiante: "))
                            iD_estudiante = int(input(f"Ingresa el ID de {nombre_estudiante}: "))
                            agregar_estudiante(nombre_estudiante, iD_estudiante)
                    except:
                        print("Error!!, debe ingresar los datos de forma correcta.")
                case 2:
                    try:
                        iD_estudiante = int(input(f"Ingresa el ID de su estuadiente a eliminar: "))
                        eliminar_estudiante(iD_estudiante)
                    except:
                        print("Error!!, ID no encontrado.")
                case 3:
                    # muestra los estudiantes de forma ordenada:
                    listar_estudiantes()
                case 4:
                    try:
                        iD_estudiante = int(input(f"Ingresa el ID de su estuadiente a bucar: "))
                        buscar_estudiante(iD_estudiante)
                    except:
                        print("Error!!, ID no encontrado.")
                case _:
                    print("Error!!, opcion no valida, vuelva a intentarlo.")
=======
            print("Opciones de estudiantes: 1: agregar, 2: eliminar, 3: listar, 4: buscar")
>>>>>>> f2bad45238d7151b5463c04ec3533d9c1d2d693a
        elif opcion == "2":
            print("Opciones de estudiantes: 1: agregar, 2: eliminar, 3: listar, 4: buscar")
            op = int(input("Que quieres realizar: "))
            if op == 1:
                Veces = int(input("cuantos Maestro Quieres agregar: "))
                for i in range(Veces):
                    nombre = input("Nombre del Maestro: ")
                    id_maestro = input("ID del Maestro: ")
                    agregar_maestro(nombre, id_maestro)
            if op == 2:
                id_maestro = input("ID Del Maestro que quiere Eliminar: ")
                eliminar_maestro(id_maestro)
            if op == 3:
                listar_maestros()
            if op == 4:
                id_maestro = input("Id del Maestro para buscarlo: ")
                buscar_maestro(id_maestro)
        elif opcion == "3":
            print("Opciones de cursos: agregar, eliminar, listar, asignar maestro")


        elif opcion == "4":
            print("Opciones de notas")
            print("1: agregar    2: listar   3: promedio      4: mejores")
            op = int(input("Que Opcion desea Realizar: "))
            if op == 1:
                id_estudiante = input("Id del estudiante Al que va agregar la nota: ")
                id_curso = input("Id Del curso del estuidantes: ")
                nota = float(int("Nota del Estudiante: "))
                agregar_nota(id_estudiante, id_curso, nota)
            if op == 2:
                id_estudiante = input("Id del estudiante para ver la notas: ")
                listar_notas_estudiante(id_estudiante)
            if op == 3:
                id_estudiante = input("Id del estudiante para ver la notas: ")
                calcular_promedio(id_estudiante)
            if op == 4:
                id_curso =  input("Id del curso: ")
                mejores_estudiantes(id_curso, n=5)

        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

# ==============================
# INICIO DEL PROGRAMA
# ==============================
if __name__ == "__main__":
    cargar_datos()
    menu_principal()
    guardar_datos()


