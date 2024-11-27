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

def selection_sort(arreglo):
    """Implementa el algoritmo de Selection Sort."""
    n = len(arreglo)
    if n == 0:
        print("El arreglo está vacío. No se puede ordenar.")
        return

    for i in range(n):
        # Encontrar el índice del elemento mínimo en el resto del arreglo
        minimo = i
        for j in range(i + 1, n):
            if arreglo[j] < arreglo[minimo]:
                minimo = j
        # Intercambiar el elemento mínimo con el elemento actual
        arreglo[i], arreglo[minimo] = arreglo[minimo], arreglo[i]

def imprimir_arreglo(arreglo):
    """Imprime el arreglo."""
    print(" ".join(map(str, arreglo)))

if __name__ == "__main__":
    # Tamaños de prueba
    tamanos = [100, 1000, 10000, 100000]
    tamanos = [100, 1000, 10000, 100000]

    for tamano in tamanos:
        print(f"\nGenerando arreglo de tamaño {tamano}...")
        arreglo = generar_arreglo(tamano)
        
        if tamano <= 100:  # Imprimir solo arreglos pequeños
            imprimir_arreglo(arreglo)

        # Medir tiempo de ejecución
        if len(arreglo) > 0:  # Asegurarse de que no está vacío
            print(f"Ordenando arreglo de tamaño {tamano} con Selection Sort...")
            inicio = time.time()
            selection_sort(arreglo)
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