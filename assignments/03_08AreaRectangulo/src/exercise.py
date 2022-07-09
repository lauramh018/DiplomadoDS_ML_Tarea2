base = float(input('Dame la base:'))
altura = float(input('Dame la altura:'))

def area_rectangulo(base,altura):
    area = base * altura
    return area

def main() :
    #escribe tu código abajo de esta línea
    print (f'El área del rectámgulo es: {area_rectangulo(base,altura)}')



if __name__=='__main__':
    main()
