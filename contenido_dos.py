print("-------------------------------------------")

name=input("Digita tu nombre: ")
if (name == "Alice"):
    print("Hola Alice")
elif(name == "Angela"):
     print("Hola Angela")
else:
    print("No eres Alice")

print("-------------------------------------------")

try:
    num1 =  int(input("Ecribe un numero:"))
except:
    print("Dato incorrecto")

num2 =  int(input("Ecribe otro numero:"))
num3 =  int(input("Ecribe otro numero:"))
          
if(num1==num2 or num2==num3 or num1==num3):
    print(f"Hay numeros repartidos")

if(num1==num2 and num1>num3):
    print(f"El numero mayor es: {num1}")

elif (num2>num1 and num2>num3):
    print(f"El numero mayor es: {num2}")
    A
elif (num3>num1 and num3>num2):
    print(f"El numero mayor es: {num3}")

else:
    print(f"Los tres son iguales")

print("-------------------------------------")



