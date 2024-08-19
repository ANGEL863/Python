
class Cliente:
    def __init__(self, nombre, apellido, telefono, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.mascotas = []  # Lista para almacenar las mascotas del cliente

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_mascotas(self):
        print("Mascotas de", self.nombre, self.apellido)
        for mascota in self.mascotas:
            print(f"- {mascota.especie}, {mascota.raza}, {mascota.fecha_nacimiento}")

class Mascota:
    def __init__(self, especie, raza, fecha_nacimiento):
        self.especie = especie
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento

# Instanciación y uso
cliente1 = Cliente("Pedro", "Lopez", "123456789", "Calle Falsa 123")

mascota1 = Mascota("Perro", "Pitbull", "2024-05-28")
mascota2 = Mascota("Gato", "Siamés", "2024-07-10")

cliente1.registrar_mascota(mascota1)
cliente1.registrar_mascota(mascota2)

cliente1.mostrar_mascotas()
