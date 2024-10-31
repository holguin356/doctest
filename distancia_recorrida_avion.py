# un avión viaja de manera rectilinea a 800 millas por hora. cuanta distancia recorrio en km en un tercio de hora
velAvion = 800
def conversionKmMilla(millas:float):
    """
    convierte millas a kilometros

    Args:
        millas(float): cantidad de millas a convertir

    returns:
        float: la cantidad equivalente a kilometros

    >>> conversionKmMilla(1)
    1.60934
    >>> conversionKmMilla(2)
    3.21868
    """
    return millas * 1.60934
velAvionKm = conversionKmMilla(velAvion)
tiempoRecorrido = 1/3
def distanciaRecorrida(velocidad:float, tiempo:float):
    """
    Indica la distancia recorrida

    Args:
        velocidad(float): velocidad rectilina del cuerpo
        tiempo(float): tiempo en medida de hora 

    returns:
        float: distancia recorrida en km

    ejemplo:
    >>> distanciaRecorrida(1, 1)
    1
    """
    return velocidad * tiempo

print(f"la distancia recorrida es: {distanciaRecorrida(velAvionKm, tiempoRecorrido):.2f} km")

if __name__ == "__main__":
    import doctest
    doctest.testmod()