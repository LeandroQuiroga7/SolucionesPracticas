print('\n' + '- Sistema de Agenda Telefónica -' + '\n')

agenda_telefonica = {}
opcion_seleccionada = 0

print('¡Bienvenido a la Agenda Telefónica!')

while opcion_seleccionada != 5:
    print('Menú de opciones:')
    print('1.- Agregar una persona.')  # Esta opción agrega una persona (apellido, nombre, dni, email y número de teléfono) al diccionario a la persona que el usuario ingrese.
    print('2.- Modificar una persona.')  # Dado su dni debe buscar la persona y preguntar si desea cambiar los demás campos de la persona, cambiando los que quiera.
    print('3.- Eliminar una persona.')  # Elimina según el DNI.
    print('4.- Mostrar todos la agenda.')  # Muestra todos los contactos de la agenda.
    print('5.- Salir.')  # Sale del programa.

    opcion_seleccionada = int(input('¿Qué desea hacer? Ingrese el número de opción deseada: '))

    if opcion_seleccionada == 1:
        print('Opción 1: Agregar una persona.')
        apellido = input('Ingrese el apellido de la persona: ')
        nombre = input('Ingrese el nombre de la persona: ')
        dni = int(input('Ingrese el DNI de la persona: '))
        email = input('Ingrese el email de la persona: ')
        telefono = int(input('Ingrese el número de teléfono de la persona: '))

        agenda_telefonica[dni] = {
            'apellido': apellido,
            'nombre': nombre,
            'email': email,
            'telefono': telefono,
        }
        print('La persona ha sido agregada a la agenda.')
    elif opcion_seleccionada == 2:
        print('Opción 2: Modificar una persona.')
        dni = int(input('Ingrese el DNI de la persona a modificar: '))
        if dni in agenda_telefonica:
            print('Persona encontrada.')
            print(agenda_telefonica[dni])
            modificar = input('¿Desea modificar los datos de la persona? (s/n)')
            if modificar == 's':
                apellido = input('Ingrese el nuevo apellido de la persona: ')
                nombre = input('Ingrese el nuevo nombre de la persona: ')
                email = input('Ingrese el nuevo email de la persona: ')
                telefono = int(input('Ingrese el nuevo número de teléfono de la persona: '))

                agenda_telefonica[dni] = {
                    'apellido': apellido,
                    'nombre': nombre,
                    'email': email,
                    'telefono': telefono,
                }
                print('La persona ha sido modificada.')
            else:
                print('La persona no ha sido modificada.')
        else:
            print('Persona no encontrada.')
    elif opcion_seleccionada == 3:
        print('Opción 3: Eliminar una persona.')
        dni = int(input('Ingrese el DNI de la persona a eliminar: '))
        if dni in agenda_telefonica:
            print('Persona encontrada.')
            print(agenda_telefonica[dni])
            eliminar = input('¿Desea eliminar a la persona? (s/n)')
            if eliminar == 's':
                del agenda_telefonica[dni]
                print('La persona ha sido eliminada de la agenda.')
            else:
                print('La persona no ha sido eliminada.')
        else:
            print('Persona no encontrada.')
    elif opcion_seleccionada == 4:
        print('Opción 4: Mostrar todos los contactos de la agenda.')
        print(agenda_telefonica)
    elif opcion_seleccionada == 5:
        print('Opción 5: Salir.')
        print('¡Hasta luego!')
    else:
        print('Opción no válida. Intente nuevamente.')
