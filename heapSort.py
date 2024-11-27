import random
import time

def generar_arreglo(tamano):
    """Genera un arreglo de números aleatorios de tamaño 'tamano'."""
    if tamano <= 0:
        print("Tamaño inválido. Generando arreglo vacío.")
        return []
    arreglo = list(range(1, tamano + 1))
    random.shuffle(arreglo)
    return arreglo

def heapify(arreglo, n, i):
    """Mantiene la propiedad del heap para un nodo dado."""
    largest = i  # Inicializar como raíz
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2  # Hijo derecho

    # Si el hijo izquierdo es mayor que la raíz
    if left < n and arreglo[left] > arreglo[largest]:
        largest = left

    # Si el hijo derecho es mayor que el nodo más grande hasta ahora
    if right < n and arreglo[right] > arreglo[largest]:
        largest = right

    # Si el más grande no es la raíz
    if largest != i:
        arreglo[i], arreglo[largest] = arreglo[largest], arreglo[i]  # Intercambio
        heapify(arreglo, n, largest)  # Recursivamente heapificar el subárbol afectado

def heap_sort(arreglo):
    """Implementa el algoritmo de Heap Sort."""
    n = len(arreglo)

    # Construir el heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arreglo, n, i)

    # Extraer elementos uno por uno del heap
    for i in range(n - 1, 0, -1):
        arreglo[i], arreglo[0] = arreglo[0], arreglo[i]  # Mover la raíz actual al final
        heapify(arreglo, i, 0)

def imprimir_arreglo(arreglo):
    """Imprime el arreglo."""
    print(" ".join(map(str, arreglo)))

if __name__ == "__main__":
    # Tamaños de prueba
    tamanos = [100, 1000, 10000, 100000]

    for tamano in tamanos:
        print(f"\nGenerando arreglo de tamaño {tamano}...")
        arreglo = generar_arreglo(tamano)
        
        if tamano <= 100:  # Imprimir solo arreglos pequeños
            imprimir_arreglo(arreglo)

        # Medir tiempo de ejecución
        if len(arreglo) > 0:  # Asegurarse de que no está vacío
            print(f"Ordenando arreglo de tamaño {tamano} con Heap Sort...")
            inicio = time.time()
            heap_sort(arreglo)
            fin = time.time()

            # Calcular tiempo total
            tiempo_ejecucion = fin - inicio
            print(f"Tiempo de ejecución para tamaño {tamano}: {tiempo_ejecucion:.6f} segundos")
            
            if tamano <= 100:  # Imprimir solo arreglos pequeños
                print("\nArreglo ordenado:")
                imprimir_arreglo(arreglo)
            else:
                print("Ordenamiento completado.\n")
        else:
            print("No se puede ordenar un arreglo vacío.")
