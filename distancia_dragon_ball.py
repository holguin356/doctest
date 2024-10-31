#Goku y Ginyu van uno tras de otro, el primer viaja a 400 pies/s el segundo viaja a 100 metros/s, si se encuentran a 2000 kilometros en un momento inicial, cuanto se demoran en encontrarse
import doctest

gokuVelocidadpiesSeg = 400
gyniuVelocidadMetrosSeg = 100
valorConversionPiesMetros = 0.3048
valorConversionkilometrosMetros = 1000
distanciakilometro = 2000

# funciones
def conversion(factor:float, conversion:float):
    """
    Convierte una media en pies a metros

    Args:
    velocidad: medida de velocidad en pies
    conversion: formula de conversion

    >>> conversion(10, 0.3048)
    3.048
    >>> conversion(10, valorConversionPiesMetros)
    3.048
    >>> conversion(20, valorConversionPiesMetros)
    6.096
    """
    return factor * conversion
doctest.testmod()

def tiempoEncontrarse(distanciaMetros:float, velocidadMetros1:float, velocidadMetros2:float):
    """
    Tiempo que se demoran en encontrarse dos objetos

    Args:
    distanciaMetros: distancia a la cual estan los dos objetos
    velocidadMetros1: velocidad en metros sobre seg del objeto 1
    velocidadMetros2: velocidad en metros sobre seg del objeto 2

    >>> tiempoEncontrarse(100, 50, 50)
    1.0
    >>> tiempoEncontrarse(2000, 500, 500)
    2.0
    """
    return distanciaMetros/(velocidadMetros1 + velocidadMetros2)
    

gokuVelocidadMetroSeg = conversion(gokuVelocidadpiesSeg, valorConversionPiesMetros)
distanciaMetro = conversion(distanciakilometro, valorConversionkilometrosMetros)
print(f"El tiempo en encontrarse Goku y el capitan Gyniu es: {tiempoEncontrarse(distanciaMetro, gokuVelocidadMetroSeg, gyniuVelocidadMetrosSeg)} segundos")
print(f"{tiempoEncontrarse(distanciaMetro, gokuVelocidadMetroSeg, gyniuVelocidadMetrosSeg)/60} minutos")


