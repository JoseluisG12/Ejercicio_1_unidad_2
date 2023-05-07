from ClaseEmail import Email
import csv
class lista:
    Emails = []

    def __init__(self):
        self.__Emails = []

    def crearcuentas (self):
        archivo = open('correos.csv')
        reader = csv.reader(archivo, delimiter=',')
        i = 0

        for fila in reader:

            if fila[0].find('@') == -1:
                print('el correo {} no es  valido para almacenar'.format(fila[0]))
                i = i + 1
            else:
                bloque = fila[0].split('@')
                ide = bloque[0]
                bloque2 = bloque[1].split('.')
                dominio = bloque2[0]
                bloque3 = bloque2[1].split('.')
                tipo = bloque3[0]
                em = Email(ide,dominio,tipo)
                self.__Emails.append(em)
            fila.pop(0)
            i = i + 1
    def buscardominio(self,dom):
        b = 0
        for i in range(len(self.__Emails)):

             if self.__Emails[i].getdominio() == dom:
                   b = b + 1

        return b











