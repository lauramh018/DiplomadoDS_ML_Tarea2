#Escribe aqui tus funciones
tipo_silla = input('Indica el tipo de silla a comprar (B/E/L): ').upper()
cantidad = int(input('Indica la cantidad: '))
tipo_cliente = input('Indica el tipo de cliente (F/N): ').upper()

def total_antes_descuento(tipo_silla,cantidad):
    

    if tipo_silla == 'B':
        total = 700*cantidad

    elif tipo_silla == 'E':
        total = 900*cantidad

    elif tipo_silla == 'L':
        total = 1500*cantidad
    else:
        print('Datos incorrectos')

    return total



def calcula_descuento(total,tipo_cliente):

    total = total_antes_descuento(tipo_silla,cantidad)

    if tipo_cliente == 'F':
        descuento = total * .8
        
    elif tipo_cliente == 'N' and total >= 10000 and total < 20000:
        descuento = total *.9

    elif tipo_cliente == 'N' and total >= 20000:
        descuento = total*.85
    else:
        descuento = total
    
    return(descuento)
      
def main() :
    #calcula_descuento(total_antes_descuento(tipo_silla,cantidad),tipo_cliente)

    print(f'Tipo de silla: {tipo_silla}')
    print(f'Tipo de cliente: {tipo_cliente}')
    print(f'Cantidad de sillas: {cantidad}')
    print(f'Total sin dcto: {total_antes_descuento(tipo_silla,cantidad)}')
    print(f'Total a pagar: {calcula_descuento(total_antes_descuento(tipo_silla,cantidad),tipo_cliente)}')

if __name__=='__main__':
    main()
