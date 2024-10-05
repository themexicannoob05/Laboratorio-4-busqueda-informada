import heapq
import time


# Algoritmo A* para el laberinto complejo
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


# Laberinto complejo
laberinto_complejo = [
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

inicio_complejo = (0, 1)
fin_complejo = (5, 12)

# Medición del tiempo de ejecución para el laberinto complejo
tiempo_inicio_complejo = time.perf_counter()
camino_complejo = a_estrella(laberinto_complejo, inicio_complejo, fin_complejo)
tiempo_fin_complejo = time.perf_counter()

print("\nCamino del laberinto complejo:", camino_complejo)
print("Tiempo de ejecución para el laberinto complejo:", tiempo_fin_complejo - tiempo_inicio_complejo, "segundos")
