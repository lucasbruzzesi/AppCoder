dpagocliente = {'Nombre titular\n':[],
                'Numero de tarjeta\n':[],
                'Vencimiento\n':[],
                'Codigo de seguridad\n':[]}


def pagar(pago):
    nombre_titular = input('Ingrese nombre del titular: ')
    nro_tarjeta = input('Ingrese el numero de la tarjeta sin espacios: ')
    vto = input('Ingrese el vencimiento en formato dd/mm: ')
    cvv = input('Ingrese el codigo de seguridad: ')

    pago['Nombre titular'].append(nombre_titular)
    pago['Numero de tarjeta'].append(nro_tarjeta)
    pago['Vencimiento'].append(vto)
    pago['Codigo de seguridad'].append(cvv)

    return pago

dpagocliente=pagar(dpagocliente)
print(dpagocliente)

