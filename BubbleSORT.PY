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

def bubble_sort(arreglo):
    """Implementa el algoritmo de Bubble Sort."""
    n = len(arreglo)
    if n == 0:
        print("El arreglo está vacío. No se puede ordenar.")
        return
    
    for i in range(n):
        # Realizar n - i - 1 comparaciones en cada pasada
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                # Intercambiar elementos si están en el orden incorrecto
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

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
            print(f"Ordenando arreglo de tamaño {tamano} con Bubble Sort...")
            inicio = time.time()
            bubble_sort(arreglo)
            fin = time.time()

            # Calcular tiempo total
            tiempo_ejecucion = fin - inicio
            print(f"Tiempo de ejecución para tamaño {tamano}: {tiempo_ejecucion:.6f} segundos")
            
            if tamano <= 100:  # Imprimir solo arreglos pequeños para ver como se ordenan
                print("\nArreglo ordenado:")
                imprimir_arreglo(arreglo)
            else:
                print("Ordenamiento completado.\n")
        else:
            print("No se puede ordenar un arreglo vacío.")
