from Cliente import Cliente
from LoginUsuarios import *

Cliente1 = Cliente(
    input('Ingresar nombre: ').capitalize(),
    input('Ingresar apellido: ').capitalize(),
    input('Ingresar pais: ').capitalize(),
    input('Ingresar ciudad: ').capitalize(),
    input('Ingresar direccion: ').capitalize(),
    input('Ingresar mail: '),
    input('Ingresar celular: '),
    input('Ingresar tipo de tarjeta: ').capitalize()
    )

Cliente1.reserva()
Cliente1.compra()
Cliente1.envio()

print(registro)
print(Cliente1)