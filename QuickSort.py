
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

def quick_sort(arreglo):
    """Implementa el algoritmo de Quick Sort."""
    if len(arreglo) <= 1:
        return arreglo
    else:
        # Seleccionar un pivote (último elemento en este caso)
        pivote = arreglo[len(arreglo) // 2]
        menores = [x for x in arreglo if x < pivote]
        iguales = [x for x in arreglo if x == pivote]
        mayores = [x for x in arreglo if x > pivote]
        return quick_sort(menores) + iguales + quick_sort(mayores)

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
            print(f"Ordenando arreglo de tamaño {tamano} con Quick Sort...")
            inicio = time.time()
            arreglo_ordenado = quick_sort(arreglo)
            fin = time.time()

            # Calcular tiempo total
            tiempo_ejecucion = fin - inicio
            print(f"Tiempo de ejecución para tamaño {tamano}: {tiempo_ejecucion:.6f} segundos")
            
            if tamano <= 100:  # Imprimir solo arreglos pequeños
                print("\nArreglo ordenado:")
                imprimir_arreglo(arreglo_ordenado)
            else:
                print("Ordenamiento completado.\n")
        else:
            print("No se puede ordenar un arreglo vacío.")
