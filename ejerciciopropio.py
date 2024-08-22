class Tarea:
    def __init__(self, titulo, descripcion, responsable, fecha_limite):
        self.titulo = titulo
        self.descripcion = descripcion
        self.responsable = responsable
        self.estado = "pendiente"
        self.fecha_limite = fecha_limite

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"El estado de la tarea '{self.titulo}' ha sido actualizado a '{self.estado}'.")

    def mostrar_info(self):
        print(f"Título: {self.titulo}\nDescripción: {self.descripcion}\nResponsable: {self.responsable}\nEstado: {self.estado}\nFecha Límite: {self.fecha_limite}\n")

class Equipo:
    def __init__(self):
        self.miembros = []
        self.tareas = []

    def agregar_miembro(self, nombre):
        self.miembros.append(nombre)
        print(f"Miembro '{nombre}' agregado al equipo.")

    def asignar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea.titulo}' asignada a '{tarea.responsable}'.")

    def actualizar_tarea(self, titulo, nuevo_estado):
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                tarea.actualizar_estado(nuevo_estado)
                return
        print(f"Tarea '{titulo}' no encontrada.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas asignadas.")
        else:
            for tarea in self.tareas:
                tarea.mostrar_info()

equipo = Equipo()

while True:
    print("\n--- Menú de Gestión de Tareas ---")
    print("1. Agregar Miembro")
    print("2. Asignar Tarea")
    print("3. Actualizar Estado de Tarea")
    print("4. Mostrar Tareas")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        nombre = input("Ingrese el nombre del miembro: ")
        equipo.agregar_miembro(nombre)
    elif opcion == '2':
        titulo = input("Ingrese el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        responsable = input("Ingrese el nombre del responsable: ")
        fecha_limite = input("Ingrese la fecha límite (YYYY-MM-DD): ")
        nueva_tarea = Tarea(titulo, descripcion, responsable, fecha_limite)
        equipo.asignar_tarea(nueva_tarea)
    elif opcion == '3':
        titulo = input("Ingrese el título de la tarea a actualizar: ")
        nuevo_estado = input("Ingrese el nuevo estado (pendiente, en progreso, completada): ")
        equipo.actualizar_tarea(titulo, nuevo_estado)
    elif opcion == '4':
        equipo.mostrar_tareas()
    elif opcion == '5':
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
