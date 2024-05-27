# 1
# Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos.

nombres = []
for i in range(10):
    nombre = input("Ingrese un nombre: ")
    if nombre in nombres:
        print("El nombre ya fue ingresado")
    else:
        nombres.append(nombre)
print(nombres)

# 2
# Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo

nombres.pop(2)
nombres.pop()
nombres.sort()
print(nombres)

# 3
# Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.

persona = {
    "nombre": "Leandro",
    "apellido": "Quiroga",
    "dni": 40386818,
    "email": "quirogaleandromanuel@gmail.com",
    "fecha_nacimiento": "12/10/1997",
}
print(persona)

# 4
# En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos (nombre, apellido, dni, email, fecha de nacimiento)

familia = {
    "persona_1": {
        "nombre": "Leandro",
        "apellido": "Quiroga",
        "dni": 40386818,
        "email": "quirogaleandromanuel@gmail.com",
        "fecha_nacimiento": "12/10/1997",
    },
    "persona_2": {
        "nombre": "Sofia",
        "apellido": "Galis",
        "dni": 40507692,
        "email": "sofiagalis@gmail.com",
        "fecha_nacimiento": "15/07/1997",
    },
    "persona_3": {
        "nombre": "Carlos",
        "apellido": "Quiroga",
        "dni": 23255923,
        "email": "quirogacarlos@gmail.com",
        "fecha_nacimiento": "01/08/1974",
    },
    "persona_4": {
        "nombre": "Virginia",
        "apellido": "Perez",
        "dni": 24649707,
        "email": "perezvirg@gmail.com",
        "fecha_nacimiento": "10/09/1975",
    }
}
print(familia)

# 5 
# Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario (input). Luego mostrar los datos de la tupla.

n = int(input("Ingrese un número: "))
pares = tuple([i for i in range(1, n*2) if i % 2 == 0])
print(pares)

