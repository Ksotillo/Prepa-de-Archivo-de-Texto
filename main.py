from usuario import Usuario

def verificar_username_existe(username):
    try:
        all_users = open('BaseDeDatos.txt', 'r').readlines()# Otra forma de acceder a un archivo
        for user in all_users:
            usuario = user[:-1].split(',') # [:-1] para quitar el salto de linea
            if usuario[0] == username:
                return True
        return False
    except FileNotFoundError:
        print('Todavia no se ha registrado ningun usuario')
        return False

def buscar_usuario(username):
    with open("BaseDeDatos.txt", "r") as bd:
        datos = bd.readlines()
    for dato in datos:
        usuario = dato[:-1].split(',') # [:-1] para quitar el salto de linea
        if usuario[0] == username:
            return Usuario(usuario[0], usuario[1], usuario[2], usuario[3])

def registrar():
    '''
    Funcion para registrar a un usuario en la base de datos
    '''
    print(
        '''
        Por favor, ingrese sus datos
        '''
    )

    username = input(
        '''
        Ingrese su username:
        '''
    )

    if verificar_username_existe(username):
        print('El usuario ya existe')
        #Buscar usuario y devolverlo
        return buscar_usuario(username)


    nombre = input(
        '''
        Ingrese su nombre completo:
        '''
    )

    edad = int(input(
        '''
        Ingrese el carnet:
        '''
    ))

    genero = input(
        '''
        Ingrese su género:
        '''
    )
    usuario = Usuario(username, nombre, edad, genero)
    with open("BaseDeDatos.txt", "a+") as bd: #El a+ es por si el archivo no se ha creado entonces se crea
        bd.write("{},{},{},{}\n".format(username, nombre, edad, genero))
    print('\tUsuario: ', usuario.username, ' registrado correctamente')
    return Usuario

def ver(edit = False):
    '''
    Funcion para ver los usuarios en la base de datos
    '''
    print(
        '''
        Estos son los usuarios registrados actualmente:
        '''
    )
    usuarios = []
    with open("BaseDeDatos.txt", "r") as bd:
        datos = bd.readlines()
    for dato in datos:
        usuario = dato[:-1].split(',') # [:-1] para quitar el salto de linea
        usuarios.append(Usuario(usuario[0], usuario[1], usuario[2], usuario[3]))
        #print(i+1, " - Estudiante {} de {} años, titular de la cedula {} y el carnet {} estudia {}".format(estudiante.nombre, estudiante.edad, estudiante[1], estudiante[2], estudiante[3]))
    #usuarios = sorted(usuarios, key= lambda user: user.username)
    if not edit:
        usuarios.sort(key= lambda user: user.username)
    for i, user in enumerate(usuarios):
        print('-'*5, i+1, '-'*5)
        print(user)


def actualizar(seleccion):
    '''
    Funcion que permite actualizar atributos de los usuarios registrados en la base de datos
    '''
    print('''
    ¿Qué atributo desea modificar?

    1 - Username
    2 - Nombre
    3 - Edad
    4 - Género
    ''')
    selec  = int(input('''
    Seleccione una opción
    '''))

    with open("BaseDeDatos.txt", 'r') as bd:
        datos = bd.readlines()
        usuario = datos[seleccion - 1][:-1].split(',')
    usuario[selec - 1] = input("Ingrese el nuevo valor:")
    nuevo_valor = ''
    for i in range(len(usuario)):
        if i != len(usuario) -1:
            nuevo_valor += usuario[i] + ','
        else:
            nuevo_valor += usuario[i] + '\n'
    datos[seleccion - 1] = nuevo_valor
    with open("BaseDeDatos.txt", "w") as bd:
        bd.writelines(datos)

def eliminar(seleccion):
    '''
    Funcion para eliminar un usuario de la base de datos
    '''
    with open("BaseDeDatos.txt", "r") as bd:
        lines = bd.readlines()
        suprimir = lines[seleccion - 1]
    with open("BaseDeDatos.txt", "w") as bd:
        for line in lines:
            if line != suprimir:
                bd.write(line)

def main():
    print("Bienvenido al sistema de registro de usuarios de mi juego de Batalla Naval")

    print('''
    ¿Qué operación desea realizar?

    1 - Registrar un usuario
    2 - Ver un usuario
    3 - Actualizar un usuario
    4 - Eliminar un usario
    ''')

    seleccion = int(input('''
    Seleccione una opción: (1/2/3/4) \n
    '''))

    if seleccion == 1:
        usuario = registrar()
        print(usuario)
    elif seleccion == 2:
        ver()
    elif seleccion == 3:
        ver(edit = True)
        seleccion = int(input("Seleccione el usuario que desee actualizar: "))
        actualizar(seleccion)
    elif seleccion == 4:
        ver()
        seleccion = int(input("Seleccione el usuario que desee eliminar: "))
        eliminar(seleccion)
    else:
        print("Seleccione una opción correcta.")

main()