# ==============================
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
# Función para mostrar encabezados bonitos
# ------------------------------
def mostrar_encabezado(texto):
    ancho = 50
    print("\n" + "=" * ancho)
    print(texto.center(ancho))
    print("=" * ancho)

# ------------------------------
# Funciones de gestión de estudiantes
# ------------------------------
def agregar_estudiante(nombre, id_estudiante):
    estudiantes[id_estudiante] = nombre
    print(f"Estudiante {nombre} agregado con ID {id_estudiante}.")

def eliminar_estudiante(id_estudiante):
    if id_estudiante in estudiantes:
        del estudiantes[id_estudiante]
        print(f"Estudiante con ID {id_estudiante} eliminado.")
    else:
        print("Estudiante no encontrado.")

def listar_estudiantes():
    mostrar_encabezado("LISTA DE ESTUDIANTES")
    if not estudiantes:
        print("No hay estudiantes registrados.")
    for id_est, nombre in estudiantes.items():
        print(f"ID: {id_est} | Nombre: {nombre}")

def buscar_estudiante(id_estudiante):
    return estudiantes.get(id_estudiante, "Estudiante no encontrado")

# ------------------------------
# Funciones de gestión de maestros
# ------------------------------
def agregar_maestro(nombre, id_maestro):
    maestros[id_maestro] = nombre
    print(f"Maestro {nombre} agregado con ID {id_maestro}.")

def eliminar_maestro(id_maestro):
    if id_maestro in maestros:
        del maestros[id_maestro]
        print(f"Maestro con ID {id_maestro} eliminado.")
    else:
        print("Maestro no encontrado.")

def listar_maestros():
    mostrar_encabezado("LISTA DE MAESTROS")
    if not maestros:
        print("No hay maestros registrados.")
    for id_m, nombre in maestros.items():
        print(f"ID: {id_m} | Nombre: {nombre}")

def buscar_maestro(id_maestro):
    return maestros.get(id_maestro, "Maestro no encontrado")

# ------------------------------
# Funciones de gestión de cursos
# ------------------------------
def agregar_curso(nombre_curso, id_curso):
    cursos[id_curso] = {"nombre": nombre_curso, "maestro": None}
    print(f"Curso {nombre_curso} agregado con ID {id_curso}.")

def eliminar_curso(id_curso):
    if id_curso in cursos:
        del cursos[id_curso]
        print(f"Curso con ID {id_curso} eliminado.")
    else:
        print("Curso no encontrado.")

def listar_cursos():
    mostrar_encabezado("LISTA DE CURSOS")
    if not cursos:
        print("No hay cursos registrados.")
    for id_c, info in cursos.items():
        maestro = info["maestro"] or "Sin asignar"
        print(f"ID: {id_c} | Nombre: {info['nombre']} | Maestro: {maestro}")

def asignar_maestro_curso(id_maestro, id_curso):
    if id_curso in cursos and id_maestro in maestros:
        cursos[id_curso]["maestro"] = maestros[id_maestro]
        print(f"Maestro {maestros[id_maestro]} asignado al curso {cursos[id_curso]['nombre']}.")
    else:
        print("Curso o maestro no encontrado.")

# ------------------------------
# Funciones de notas
# ------------------------------
def agregar_nota(id_estudiante, id_curso, nota):
    if id_estudiante not in estudiantes or id_curso not in cursos:
        print("Estudiante o curso no encontrado.")
        return
    notas.setdefault(id_curso, {})
    notas[id_curso].setdefault(id_estudiante, [])
    notas[id_curso][id_estudiante].append(nota)
    print(f"Nota {nota} agregada para {estudiantes[id_estudiante]} en {cursos[id_curso]['nombre']}.")

def listar_notas_estudiante(id_estudiante):
    mostrar_encabezado(f"NOTAS DE {estudiantes.get(id_estudiante, 'Desconocido')}")
    encontrado = False
    for id_c, estudiantes_curso in notas.items():
        if id_estudiante in estudiantes_curso:
            print(f"{cursos[id_c]['nombre']}: {estudiantes_curso[id_estudiante]}")
            encontrado = True
    if not encontrado:
        print("Este estudiante no tiene notas registradas.")

def calcular_promedio(id_estudiante):
    total, count = 0, 0
    for estudiantes_curso in notas.values():
        if id_estudiante in estudiantes_curso:
            total += sum(estudiantes_curso[id_estudiante])
            count += len(estudiantes_curso[id_estudiante])
    if count == 0:
        print("No hay notas registradas para este estudiante.")
        return None
    promedio = total / count
    print(f"Promedio del estudiante {estudiantes[id_estudiante]}: {promedio:.2f}")
    return promedio

def mejores_estudiantes(id_curso, n=5):
    if id_curso not in notas:
        print("No hay notas registradas para este curso.")
        return
    promedio_estudiantes = {id_est: sum(lista) / len(lista) for id_est, lista in notas[id_curso].items()}
    mejores = sorted(promedio_estudiantes.items(), key=lambda x: x[1], reverse=True)[:n]
    mostrar_encabezado(f"MEJORES ESTUDIANTES DEL CURSO {cursos[id_curso]['nombre']}")
    for id_est, prom in mejores:
        print(f"{estudiantes[id_est]} - Promedio: {prom:.2f}")

# ------------------------------
# Funciones de utilidad
# ------------------------------
def guardar_datos():
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

# ------------------------------
# Menú principal
# ------------------------------
def menu_principal():
    while True:
        mostrar_encabezado("SISTEMA ESCOLAR")
        print("1. Gestionar Estudiantes")
        print("2. Gestionar Maestros")
        print("3. Gestionar Cursos")
        print("4. Gestionar Notas")
        print("5. Salir")
        print("=" * 50)
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_encabezado("GESTIÓN DE ESTUDIANTES")
            print("1. Agregar | 2. Eliminar | 3. Listar | 4. Buscar")
            op = int(input("Elige una opción: "))
            if op == 1:
                cantidad = int(input("¿Cuántos estudiantes deseas ingresar?: "))
                for i in range(cantidad):
                    nombre = input("Nombre del estudiante: ")
                    id_est = input("ID del estudiante: ")
                    agregar_estudiante(nombre, id_est)
            elif op == 2:
                id_est = input("ID del estudiante a eliminar: ")
                eliminar_estudiante(id_est)
            elif op == 3:
                listar_estudiantes()
            elif op == 4:
                id_est = input("ID del estudiante a buscar: ")
                print(buscar_estudiante(id_est))
            else:
                print("Opción no válida.")

        elif opcion == "2":
            mostrar_encabezado("GESTIÓN DE MAESTROS")
            print("1. Agregar | 2. Eliminar | 3. Listar | 4. Buscar")
            op = int(input("Elige una opción: "))
            if op == 1:
                cantidad = int(input("¿Cuántos maestros deseas agregar?: "))
                for i in range(cantidad):
                    nombre = input("Nombre del maestro: ")
                    id_maestro = input("ID del maestro: ")
                    agregar_maestro(nombre, id_maestro)
            elif op == 2:
                id_maestro = input("ID del maestro a eliminar: ")
                eliminar_maestro(id_maestro)
            elif op == 3:
                listar_maestros()
            elif op == 4:
                id_maestro = input("ID del maestro a buscar: ")
                print(buscar_maestro(id_maestro))
            else:
                print("Opción no válida.")

        elif opcion == "3":
            mostrar_encabezado("GESTIÓN DE CURSOS")
            print("1. Agregar | 2. Eliminar | 3. Listar | 4. Asignar Maestro")
            op = int(input("Elige una opción: "))
            if op == 1:
                cantidad = int(input("¿Cuántos cursos deseas agregar?: "))
                for i in range(cantidad):
                    nombre = input("Nombre del curso: ")
                    id_curso = input("ID del curso: ")
                    agregar_curso(nombre, id_curso)
            elif op == 2:
                id_curso = input("ID del curso a eliminar: ")
                eliminar_curso(id_curso)
            elif op == 3:
                listar_cursos()
            elif op == 4:
                id_curso = input("ID del curso: ")
                id_maestro = input("ID del maestro: ")
                asignar_maestro_curso(id_maestro, id_curso)
            else:
                print("Opción no válida.")

        elif opcion == "4":
            mostrar_encabezado("GESTIÓN DE NOTAS")
            print("1. Agregar | 2. Listar | 3. Promedio | 4. Mejores Estudiantes")
            op = int(input("Elige una opción: "))
            if op == 1:
                id_est = input("ID del estudiante: ")
                id_curso = input("ID del curso: ")
                nota = float(input("Nota del estudiante: "))
                agregar_nota(id_est, id_curso, nota)
            elif op == 2:
                id_est = input("ID del estudiante: ")
                listar_notas_estudiante(id_est)
            elif op == 3:
                id_est = input("ID del estudiante: ")
                calcular_promedio(id_est)
            elif op == 4:
                id_curso = input("ID del curso: ")
                mejores_estudiantes(id_curso, n=5)
            else:
                print("Opción no válida.")

        elif opcion == "5":
            mostrar_encabezado("SALIENDO DEL SISTEMA")
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

