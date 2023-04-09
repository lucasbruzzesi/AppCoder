class Cliente:
    
    def __init__(self, nombre, apellido, pais, ciudad, direccion, mail, telefono, tipotarjeta):
        
        self.nombre = nombre
        self.__apellido = apellido
        self.__pais = pais
        self.__ciudad = ciudad
        self.__direccion = direccion
        self.mail = mail
        self.telefono = telefono
        self.__tipotarjeta = tipotarjeta

    
    def get_tipotarjeta(self):
        return self.__tipotarjeta
    
    def get_pais(self):
        return self.__pais
    
    def get_direccion(self):
        return self.__direccion


    def reserva(self):
        print(f'\nHola {self.nombre} se necesita una reserva del 10% del valor del producto para continuar con la compra.\n')

    def compra(self):
        print(f'{self.nombre}, la compra realizada con su tarjeta {self.__tipotarjeta} terminada en xxxx-xxxx-xxxx-8794 esta siendo procesada.\n')

    def envio(self):
        print(f'Felicitaciones {self.nombre}, la compra ha sido confirmada con envio a {self.__pais}, {self.__ciudad}, direccion {self.__direccion}.\n')

    def __str__(self):
        return(f'Hola {self.nombre}, la compra del producto ha sido realizada con exito, se ha enviado un mail a {self.mail} con su comprobante de compra.\n')
