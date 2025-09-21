# ============================== Usted esta en Curso starlyn.
# SISTEMA ESCOLAR BÁSICO
# ==============================
import json
import os
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
    print(f" Estudiante {nombre} agregado con ID {id_estudiante}.")

def eliminar_estudiante(id_estudiante):
    """Elimina un estudiante del sistema"""
    if id_estudiante in estudiantes:
        del estudiantes[id_estudiante]
        print(f" Estudiante con ID {id_estudiante} eliminado.")
    else:
        print(" Estudiante no encontrado.")

def listar_estudiantes():
    """Muestra todos los estudiantes"""
    print("\n Lista de estudiantes:")
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    for id_est, nombre in estudiantes.items():
        print(f"ID: {id_est}, Nombre: {nombre}")

def buscar_estudiante(id_estudiante):
    """Busca un estudiante por ID"""
    return estudiantes.get(id_estudiante, " Estudiante no encontrado")

# ------------------------------
# Funciones de gestión de maestros
# ------------------------------
def agregar_maestro(nombre, id_maestro):
    """Agrega un maestro al sistema"""
    maestros[id_maestro] = nombre
    print(f" Maestro {nombre} agregado con ID {id_maestro}.")

def eliminar_maestro(id_maestro):
    """Elimina un maestro del sistema"""
    if id_maestro in maestros:
        del maestros[id_maestro]
        print(f" Maestro con ID {id_maestro} eliminado.")
    else:
        print(" Maestro no encontrado.")

def listar_maestros():
    """Muestra todos los maestros"""
    print("\n Lista de maestros:")
    if not maestros:
        print("No hay maestros registrados.")
        return
    for id_m, nombre in maestros.items():
        print(f"ID: {id_m}, Nombre: {nombre}")

def buscar_maestro(id_maestro):
    """Busca un maestro por ID"""
    return maestros.get(id_maestro, " Maestro no encontrado")

# ------------------------------
# Funciones de gestión de cursos
# ------------------------------
def agregar_curso(nombre_curso, id_curso):
    """Agrega un curso al sistema"""
    cursos[id_curso] = {"nombre": nombre_curso, "maestro": None}
    print(f" Curso {nombre_curso} agregado con ID {id_curso}.")

def eliminar_curso(id_curso):
    """Elimina un curso del sistema"""
    if id_curso in cursos:
        del cursos[id_curso]
        print(f" Curso con ID {id_curso} eliminado.")
    else:
        print(" Curso no encontrado.")

def listar_cursos():
    """Muestra todos los cursos"""
    print("\n Lista de cursos:")
    if not cursos:
        print("No hay cursos registrados.")
        return
    for id_c, info in cursos.items():
        maestro = info["maestro"] or "Sin asignar"
        print(f"ID: {id_c}, Nombre: {info['nombre']}, Maestro: {maestro}")

def asignar_maestro_curso(id_maestro, id_curso):
    """Asocia un maestro a un curso"""
    if id_curso in cursos and id_maestro in maestros:
        cursos[id_curso]["maestro"] = maestros[id_maestro]
        print(f" Maestro {maestros[id_maestro]} asignado al curso {cursos[id_curso]['nombre']}.")
    else:
        print(" Curso o maestro no encontrado.")

# ------------------------------
# Funciones de notas
# ------------------------------
def agregar_nota(id_estudiante, id_curso, nota):
    """Agrega una nota para un estudiante en un curso"""
    if id_estudiante not in estudiantes or id_curso not in cursos:
        print(" Estudiante o curso no encontrado.")
        return
    notas.setdefault(id_curso, {})
    notas[id_curso].setdefault(id_estudiante, [])
    notas[id_curso][id_estudiante].append(nota)
    print(f" Nota {nota} agregada para {estudiantes[id_estudiante]} en {cursos[id_curso]['nombre']}.")

def listar_notas_estudiante(id_estudiante):
    """Muestra todas las notas de un estudiante"""
    if id_estudiante not in estudiantes:
        print(" Estudiante no encontrado.")
        return
    print(f"\n Notas de {estudiantes[id_estudiante]}:")
    encontrado = False
    for id_c, estudiantes_curso in notas.items():
        if id_estudiante in estudiantes_curso:
            encontrado = True
            print(f"{cursos[id_c]['nombre']}: {estudiantes_curso[id_estudiante]}")
    if not encontrado:
        print("No tiene notas registradas.")

def calcular_promedio(id_estudiante):
    """Calcula el promedio de todas las notas de un estudiante"""
    total = 0
    count = 0
    for estudiantes_curso in notas.values():
        if id_estudiante in estudiantes_curso:
            total += sum(estudiantes_curso[id_estudiante])
            count += len(estudiantes_curso[id_estudiante])
    if count == 0:
        print(" No hay notas para este estudiante.")
        return
    promedio = total / count
    print(f" Promedio de {estudiantes[id_estudiante]}: {promedio:.2f}")

def mejores_estudiantes(id_curso, n=5):
    """Devuelve los mejores estudiantes de un curso"""
    if id_curso not in notas or not notas[id_curso]:
        print(" No hay notas registradas para este curso.")
        return
    promedio_estudiantes = {
        id_est: sum(lista_notas) / len(lista_notas)
        for id_est, lista_notas in notas[id_curso].items()
    }
    mejores = sorted(promedio_estudiantes.items(), key=lambda x: x[1], reverse=True)[:n]
    print(f"\n Mejores estudiantes del curso {cursos[id_curso]['nombre']}:")
    for id_est, prom in mejores:
        print(f"{estudiantes[id_est]} - Promedio: {prom:.2f}")

# ------------------------------
# Guardar y cargar datos en archivos
# ------------------------------
def guardar_datos():
    with open("datos.json", "w") as f:
        json.dump({"estudiantes": estudiantes, "maestros": maestros, "cursos": cursos, "notas": notas}, f)
    print(" Datos guardados correctamente.")

def cargar_datos():
    global estudiantes, maestros, cursos, notas
    if os.path.exists("datos.json"):
        with open("datos.json", "r") as f:
            datos = json.load(f)
            estudiantes = datos["estudiantes"]
            maestros = datos["maestros"]
            cursos = datos["cursos"]
            notas = datos["notas"]
        print(" Datos cargados correctamente.")
    else:
        print(" No hay datos guardados. Comenzando con el sistema vacío.")

# ------------------------------
# Menú principal con submenús
# ------------------------------
def menu_principal():
    while True:
        print("\n---  SISTEMA ESCOLAR ---")
        print("1. Gestionar Estudiantes")
        print("2. Gestionar Maestros")
        print("3. Gestionar Cursos")
        print("4. Gestionar Notas")
        print("5. Guardar y Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            menu_estudiantes()
        elif opcion == "2":
            menu_maestros()
        elif opcion == "3":
            menu_cursos()
        elif opcion == "4":
            menu_notas()
        elif opcion == "5":
            guardar_datos()
            print(" Saliendo del sistema...")
            break
        else:
            print(" Opción no válida.")

def menu_estudiantes():
    while True:
        print("\n--- 👥 GESTIÓN DE ESTUDIANTES ---")
        print("1. Agregar estudiante")
        print("2. Eliminar estudiante")
        print("3. Listar estudiantes")
        print("4. Buscar estudiante")
        print("5. Volver")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            id_est = input("ID del estudiante: ")
            agregar_estudiante(nombre, id_est)
        elif opcion == "2":
            id_est = input("ID del estudiante a eliminar: ")
            eliminar_estudiante(id_est)
        elif opcion == "3":
            listar_estudiantes()
        elif opcion == "4":
            id_est = input("ID del estudiante a buscar: ")
            print(buscar_estudiante(id_est))
        elif opcion == "5":
            break
        else:
            print(" Opción no válida.")

def menu_maestros():
    while True:
        print("\n---  GESTIÓN DE MAESTROS ---")
        print("1. Agregar maestro")
        print("2. Eliminar maestro")
        print("3. Listar maestros")
        print("4. Buscar maestro")
        print("5. Volver")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del maestro: ")
            id_m = input("ID del maestro: ")
            agregar_maestro(nombre, id_m)
        elif opcion == "2":
            id_m = input("ID del maestro a eliminar: ")
            eliminar_maestro(id_m)
        elif opcion == "3":
            listar_maestros()
        elif opcion == "4":
            id_m = input("ID del maestro a buscar: ")
            print(buscar_maestro(id_m))
        elif opcion == "5":
            break
        else:
            print(" Opción no válida.")

def menu_cursos():
    while True:
        print("\n---  GESTIÓN DE CURSOS ---")
        print("1. Agregar curso")
        print("2. Eliminar curso")
        print("3. Listar cursos")
        print("4. Asignar maestro a curso")
        print("5. Volver")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre_curso = input("Nombre del curso: ")
            id_c = input("ID del curso: ")
            agregar_curso(nombre_curso, id_c)
        elif opcion == "2":
            id_c = input("ID del curso a eliminar: ")
            eliminar_curso(id_c)
        elif opcion == "3":
            listar_cursos()
        elif opcion == "4":
            id_c = input("ID del curso: ")
            id_m = input("ID del maestro: ")
            asignar_maestro_curso(id_m, id_c)
        elif opcion == "5":
            break
        else:
            print(" Opción no válida.")

def menu_notas():
    while True:
        print("\n---  GESTIÓN DE NOTAS ---")
        print("1. Agregar nota")
        print("2. Listar notas de estudiante")
        print("3. Calcular promedio de estudiante")
        print("4. Mostrar mejores estudiantes de un curso")
        print("5. Volver")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            id_est = input("ID del estudiante: ")
            id_c = input("ID del curso: ")
            try:
                nota = float(input("Nota: "))
                agregar_nota(id_est, id_c, nota)
            except ValueError:
                print(" Ingresa un número válido.")
        elif opcion == "2":
            id_est = input("ID del estudiante: ")
            listar_notas_estudiante(id_est)
        elif opcion == "3":
            id_est = input("ID del estudiante: ")
            calcular_promedio(id_est)
        elif opcion == "4":
            id_c = input("ID del curso: ")
            mejores_estudiantes(id_c)
        elif opcion == "5":
            break
        else:
            print(" Opción no válida.")

# ==============================
# INICIO DEL PROGRAMA
# ==============================
if __name__ == "__main__":
    cargar_datos()
    menu_principal()