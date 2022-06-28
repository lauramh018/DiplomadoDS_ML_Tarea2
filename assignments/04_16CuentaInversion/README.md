# Cálculo de intereses
Ciclos - Cálculo de intereses

En una cuenta de inversión tengo una cantidad X de dinero, el banco ofrece un rendimiento de un porcentaje de interés anual, donde cada mes el porcentaje de interés calculado se acumula al saldo de la cuenta, es decir, cada mes el saldo de la cuenta al final del mes, es igual a el saldo en ese momento más el cálculo del interés mensual.

Por ejemplo, si tienes 1000 pesos al inicio del año y el banco te da un porcentaje de rendimiento del 12% anual (es decir 1% mensual), al final de enero lo que tengo es 1010 pesos. En febrero, calculo el interés mensual pero partiendo de esos 1010 por lo que al final de febrero tendré 1020.10 y así sucesivamente cada mes.

Utiliza un ciclo for para calcular cuánto dinero voy a tener al final del año en la cuenta.   
Recuerda que el interés que se pide es anual, pero se genera mes con mes.

Si alguno de los datos, o los dos son negativos, se manda a pantalla el siguiente mensaje:
"Error en los datos"

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():    
    #escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

La salida del programa debe de ser solamente la cantidad total al final del año, y como es dinero, debe ir con dos digitos después del punto decimal:

```
Escribe la cantidad de dinero inicial : 1000
Escribe el porcentaje de interes anual : 10
1104.71
```

```
Escribe la cantidad de dinero inicial : 1000
Escribe el porcentaje de interes anual : -10
Error en los datos
```

**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.
