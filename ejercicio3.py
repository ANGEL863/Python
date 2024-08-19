
class Auto: #clase auto con su constructor y una para mostrar la informacion
    def __init__(self, modelo,tipo, marca, ano, kilometraje, precio_venta, color, transmision, placa, traccion):
        self.modelo = modelo
        self.tipo = tipo
        self.marca = marca
        self.ano = ano
        self.precio_venta = precio_venta
        self.color = color
        self.kilometraje = kilometraje
        self.transmision = transmision
        self.placa = placa
        self.traccion = traccion
        self.capacidad = "5 pasajeros"
        self.ruedas = "4 ruedas"


    def mostrar_info(self): #funcion para el formato de mostar los datos
        print("-" * 30)
        print(f"modelo: {self.modelo}")
        print(f"marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Ano: {self.ano}")
        print(f"color: {self.color}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Ruedas: {self.ruedas}")
        print(f"transmision: {self.transmision}")
        print(f"placa: {self.placa}")
        print(f"Kilometraje: {self.kilometraje}")
        print(f"Precio de Venta: ${self.precio_venta}")
        print("-" * 30)

def ingresar_autos(): #inputs del usuario
    modelo = input("Ingrese el modelo del auto: ")
    tipo = input("Ingrese el tipo del auto: ")
    marca = input("Ingrese la marca del auto: ")
    ano = int(input("Ingrese el ano del auto: "))
    kilometraje = int(input("Ingrese el kilometraje del auto: "))
    precio_compra = float(input(f"Ingrese el precio de compra del auto {modelo}: $"))
    color = input("Ingrese el color del auto: ")
    transmision = input("Ingrese la transmision del auto: ")
    placa = input("Ingrese la placa del auto: ")
    traccion = input("Ingrese la traccion del auto: ")
    precio_venta = calcular_precio_venta(precio_compra)
    return Auto(modelo, tipo, marca, ano, kilometraje, precio_venta, color, transmision, placa, traccion)

def calcular_precio_venta(precio_compra, margen=1.4): #funcion para calcular el precio de venta
    precio_venta = precio_compra * margen
    return precio_venta

# lista global
autos = []

def mostrar_autos(autos): #fucnion para mostrar los autos 
    print("\nAutos registrados:")
    for autos in autos:
        autos.mostrar_info()


def menu_principal(): #funcion para el menu principal
    while True:
        opcion = int(input("Ingrese la opcion que desea hacer: \n Opcion 1: Ingresar auto \n Opcion 2: Mostrar Autos \n Opcion 3: Salir \n"))
        if opcion == 1:
            nuevo_auto = ingresar_autos()
            autos.append(nuevo_auto)
        elif opcion == 2:
            mostrar_autos(autos)
        if opcion == 3:
            print("Gracias por utilizar el sistema")
            break

menu_principal() #ejecutar la funcion menu principal