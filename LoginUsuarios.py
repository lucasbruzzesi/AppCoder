usuarios = {}


def nuevosdatos():

    database = []

    user = input('Ingrese su nuevo usuario:\n')
    password = input('Ingrese su nueva contraseña:\n')

    database.append(completardatos(user,password))
    return database


def completardatos(user,password):
    
    usuarios['usuario'] = user
    usuarios['contraseña'] = password

    print('\nBienvenido ' + usuarios['usuario'] + ' verifica tu correo para validar tu cuenta.\n')


def verificardatos(user,password):
  
  while True:
    if usuarios['usuario']==user and usuarios['contraseña']==password:
       print('Bienvenido', usuarios['usuario'])
       return True
    else:
       print('El usuario o la contraseña son incorrectos, Intente Nuevamente')
       return False
    

def mostrardatos(usuarios):
  
    print('Su nuevo usuario es: ' + usuarios['usuario'] + ' y su contraseña: ' + usuarios['contraseña'])



registro = input('Login\n \n(1) - Crear Nuevo Usuario\n(2) - Iniciar Sesion\n(3) - Mostrar datos guardados\n(4) - Salir \n \n')

while registro != '4':
  if registro == '1':
   nuevosdatos()
   break
  if registro == '2':
    user = input('Ingrese su usuario:\n')
    password = input('Ingrese su contraseña:\n')
    verificardatos(user,password)
    break
  if registro == '3':
    mostrardatos(usuarios)
    break