 import random

 class piedra_papel_tijera():
     aleatorio = random.randrange(0,3)
     pc = ""
     print("1 - Piedra")
     print("2 - Papel")
     print("3 - Tijera")
     opcion = int(input("Elige una opcion, 1), 2) o 3):  "))

     if opcion == 1:
         usuario = "Piedra"
     elif opcion == 2:
         usuario = "Papel"
     elif opcion == 3:
         usuario = "Tijera"
     print("Elegiste" , usuario)

     if aleatorio == 0:
         pc = "Piedra"
     if aleatorio == 1:
         pc = "Papel"
     if aleatorio == 2:
         pc = "Tijera"
     print("PC a elegido ", pc)
     if pc == "Piedra" and usuario == "Papel":
         print("Usuario ha ganado, papel envuelve a la piedra")
     elif pc == "Papel" and usuario == "Tijera":
         print("Usuario ha ganado, la tijera corta al papel")
     elif pc == "Tijera" and usuario == "Piedra":
         print("Usuario ha ganado, la piedra rompe la tijera")
     elif pc == "Papel" and usuario == "Piedra":
         print("PC ha ganado, papel envuelve a la piedra")
     elif pc == "Tijera" and usuario == "Papel":
         print("PC ha ganado, la tijera corta al papel")
     elif pc == "Piedra" and usuario == "Tijera":         print("PC ha ganado, la piedra rompe a la tijera")
   elif pc == usuario:
         print("Se produjo un empate, ambos eligieron ", usuario)

 class adivinar():
    
     intentos = 0
     nombre = input("Hola, cual es tu nombre? ")
     print("Hola, ", nombre, " vamos a jugar!")
     numero = random.randint(1, 10)
    
     while intentos < 3:
         intentos += 1
         a = int(input("Elige un numero comprendido entre 1 y 10: "))
         if a == numero:
             print("Adivinaste el numero! en " + str(intentos) + " intentos")
         if a < numero: 
             print("Elegiste un numero mas bajo, segui intentando")
         if a > numero:
             print("Elegiste un numero mas alto, segui intentando")
         else:
             print("Perdiste, volve a intentar")
              break

 class dado():
     numero = random.randint(1 , 6)
     user = input("Hola, cual es tu nombre? ")
     print("Hola, ", user, " vamos a jugar!")
     opcion = input("Deseas arrojar el dado? (S / N)").upper()
     if opcion == ("S"):
         print("Ha salido el numero " + str(numero))
     else:
         print("Gracias por intentarlo!")

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.bar([1,2,3],[1,2,0.5])

plt.show()









