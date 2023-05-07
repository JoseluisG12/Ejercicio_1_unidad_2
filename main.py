
from ClaseEmail import Email
from manejadorEmail import lista

def test():
    Emcorrecto = Email("jose",'gmail','com')
    Emcorrecto.muestradatos()
    Emcorrecto.retornamail()
    Emcorrecto.crearcuenta(Emcorrecto.retornamail())
    Emcorrecto.muestradatos()
    print("Email:",Emcorrecto.retornamail())
    print(Emcorrecto.getdominio())
    Emcorrecto.verificacontraseña()
    Emcorrecto.muestradatos()
    emincorrecto = Email(1,com,'ar')
    emincorrecto.muestradatos()
    emincorrecto.retornamail()
    print(emincorrecto.getdominio())
    emincorrecto.verificacontraseña()




if __name__=='__main__':
    test()
    emails = lista()
    unusuario = Email()
    print('ingrese 1 para ingresar correo y nombre de usuario')
    print('ingrese 2 para modificar contraseña')
    print('ingrese 3 para crear cuentas atravez de un archivo csv')
    print('ingrese 4 para buscar un dominio en la lista de emails')
    print('ingrese 5 para salir')
    b = int(input('ingrese su opcion\n'))
    while b != 5:
        if (b == 1):
            nombre = input('ingrese el nombre de usuario\n')
            correo = input('ingrese su correo\n')
            unusuario.crearcuenta(correo)
            print('estimado : {}\n le enviaremos tus mensajes a la direccion:{} '.format(nombre,unusuario.retornamail()))
        elif b == 2:
            unusuario.verificacontraseña()

        elif b == 3:
            otrousuario = emails.crearcuentas()
        elif b == 4:
            dom = input('ingresar el dominio a buscar\n')
            print("el dominio {} se encontro {}".format(dom, emails.buscardominio(dom)))
        print('ingrese 1 para ingresar correo y nombre de usuario')
        print('ingrese 2 para modificar contraseña')
        print('ingrese 3 para crear cuentas atravez de un archivo csv')
        print('ingrese 4 para buscar un dominio en la lista de emails')
        print('ingrese 5 para salir')
        b =int(input('ingrese cualquier numero para reingresar'))







