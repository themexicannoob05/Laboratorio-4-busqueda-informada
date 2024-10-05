import heapq
import time


# Algoritmo A* para el primer laberinto
def a_estrella(laberinto, inicio, fin):
    def heuristica(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Distancia de Manhattan

    frontera = []
    heapq.heappush(frontera, (0, inicio))

    de_donde_viene = {inicio: None}
    costo_hasta_ahora = {inicio: 0}

    while frontera:
        actual = heapq.heappop(frontera)[1]

        if actual == fin:
            camino = []
            while actual:
                camino.append(actual)
                actual = de_donde_viene[actual]
            return camino[::-1]  # Camino en orden inverso

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            vecino = (actual[0] + dx, actual[1] + dy)
            if 0 <= vecino[0] < len(laberinto) and 0 <= vecino[1] < len(laberinto[0]) and laberinto[vecino[0]][
                vecino[1]] == 0:
                nuevo_costo = costo_hasta_ahora[actual] + 1
                if vecino not in costo_hasta_ahora or nuevo_costo < costo_hasta_ahora[vecino]:
                    costo_hasta_ahora[vecino] = nuevo_costo
                    prioridad = nuevo_costo + heuristica(vecino, fin)
                    heapq.heappush(frontera, (prioridad, vecino))
                    de_donde_viene[vecino] = actual
    return None


# Laberinto proporcionado
laberinto = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

inicio = (0, 1)
fin = (3, 4)

# Medición del tiempo de ejecución para el primer laberinto
tiempo_inicio = time.perf_counter()
camino = a_estrella(laberinto, inicio, fin)
tiempo_fin = time.perf_counter()

print("Camino:", camino)
print("Tiempo de ejecución para el primer laberinto:", tiempo_fin - tiempo_inicio, "segundos")
