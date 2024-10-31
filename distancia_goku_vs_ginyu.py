import doctest
# Conversión de kilómetros a metros
distancia_inicial_km = 2000
distancia_inicial_metros = distancia_inicial_km * 1000

# Velocidades de las partículas en m/s
velocidad_goku_1_pies = 450  # Velocidad en metros por segundo
velocidad_goku_1 = velocidad_goku_1_pies / 3.281 #velocidad metros por segundo
velocidad_ginyu = 100  # Velocidad en metros por segundo

# Función para calcular la distancia entre las partículas en cualquier momento t (en segundos)
def calcular_distancia(tiempo):
    """
    >>> calcular_distancia(0)
    2000000
    >>> calcular_distancia(3000)
    1301000
    >>> calcular_distancia(8000)
    136000
    >>> calcular_distancia(8533)
    86
    """
    distancia_recorrida = (velocidad_goku_1 + velocidad_ginyu) * tiempo
    distancia_actual = distancia_inicial_metros - distancia_recorrida
    return max(distancia_actual, 0)  # La distancia no puede ser negativa

# Ejemplo de uso
tiempo = float(input("Introduce el tiempo en segundos: "))
distancia = calcular_distancia(tiempo)

if distancia > 0:
    print(f"La distancia entre las partículas después de {tiempo} segundos es {distancia} metros.")
else:
    print("Las partículas ya se han encontrado o han pasado entre ellas.")

doctest.testmod()