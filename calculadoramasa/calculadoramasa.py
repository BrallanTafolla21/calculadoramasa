def lee_edad():
    
    while True:
        valor = input("Ingresa tu edad: ")
        try:
            valor = int(valor) 
            return valor
        except ValueError:
            print("El dato ingresado no es un numero, ingrese su edad de manera correcta. ")

def lee_peso():
    
    while True:
        valor = input("Ingresa tu peso: ")
        try:
            valor = float(valor) 
            return valor
        except ValueError:
            print("El dato ingresado no es un numero, ingrese tu peso de manera correcta. ")

def lee_estatura():
    
    while True:
        valor = input("Ingresa tu estatura en cetimetros: ")
        try:
            valor = int(valor) 
            return valor
        except ValueError:
            print("El dato ingresado no es un numero, ingresa tu estatura de manera correcta. ")

nombre = input('Ingresa tu nombre: \n')
while (len(nombre) == 0):
    nombre = input('No se detecto ningun dato\nIngrese el nombre correctamente: \n')

apellidopaterno = input('Ingresa tu apellido paterno: \n')
while (len(apellidopaterno) == 0):
    apellidopaterno = input('No se detecto ningun dato\nIngrese el apellido correctamente: \n')

apellidomaterno = input('Ingresa tu apellido materno: \n')
while (len(apellidomaterno) == 0):
    apellidomaterno = input('No se detecto ningun dato\nIngrese el apellido correctamente: \n')

edad= lee_edad()
peso=lee_peso()
estatura=lee_estatura()
imc=round(peso/(estatura/100)**2,2)

if imc >= 0 and imc <= 15.99 :
        tipo= "Delgadez severa"
elif imc >= 16.00 and imc <= 16.99 :
        tipo= "Delgadez moderada"
elif imc >= 17.00 and imc <= 18.49:
        tipo="Delgadez leve"
elif imc >= 18.50 and imc <= 24.99 :
        tipo= "Normal"
elif imc >= 25.00 and imc <= 29.99:
        tipo= "Sobrepeso"
elif imc >= 30.00 and imc <= 34.99:
        tipo= "obesidad leve"
elif imc >= 35.00 and imc <= 39.00:
        tipo= "obesidad media"
elif imc >= 40.00:
        tipo = "obesidad morbida"


print(f'Hola {nombre.title()} {apellidopaterno.title()} {apellidomaterno.title()} tu edad es {edad} anos, tu peso es de {peso} KG, con una altura de {estatura/100} Metros y tu indice de masa corporal es de {imc} segun la medida tienes {tipo}')

