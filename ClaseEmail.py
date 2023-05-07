class Email:
    __idcuenta = ''
    __dominio = ''
    __tipodominio = ''
    __contraseña = ''

    def __init__(self,x = 'id', y = 'dominio', z = 'tipodom', w = '1234'):
        self.__idcuenta = x
        self.__dominio  = y
        self.__tipodominio = z
        self.__contraseña = w
    def retornamail(self):
        return self.__idcuenta+'@'+self.__dominio+'.'+self.__tipodominio

    def getdominio(self):
        return self.__dominio

    def crearcuenta (self,correo):
        bloque = correo.split('@')
        self.__idcuenta = bloque[0]
        bloque2 = bloque[1].split('.')
        self.__dominio = bloque2[0]
        bloque3 = bloque2[1].split('.')
        self.__tipodominio = bloque3[0]
        print('contraseña por defecto 1234 despues podra modificarla si lo desea\n')
        self.__contraseña = '1234'

    def verificacontraseña(self):

        b = False
        contraseña = input('ingrese su contraseña\n')

        while b == False:

            if self.__contraseña == contraseña:
                print('contraseña correcta')
                self.__contraseña = input('ingrese contraseña nueva\n')
                b = True
            else:
                print('contraseña incorrecta')
                contraseña = input('ingrese de nuevo su contraseña\n')


    def muestradatos(self):
        print(self.__idcuenta)
        print(self.__dominio)
        print(self.__tipodominio)
        print(self.__contraseña)