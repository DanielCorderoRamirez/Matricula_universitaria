#declaracion de las variables.
edad= (int(input("digite la edad del usuario: ")))
esta_graduado= (input("el usuario esta graduado? (s/n): "))
#variables de condicionales
if edad >= 17:
    if esta_graduado == "s":
        matricula_graduado  = "bachillerato"
    else:
        matricula_graduado = "tecnico"
else: matricula_graduado = "técnico"
#impresion de la información
print(f"El programa que el intersesado puede matricularse es: {matricula_graduado}")