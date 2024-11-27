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

def merge_sort(arreglo):
    """Implementa el algoritmo de Merge Sort."""
    if len(arreglo) > 1:
        # Encuentra el punto medio
        mid = len(arreglo) // 2
        izquierda = arreglo[:mid]
        derecha = arreglo[mid:]

        # Llamada recursiva para dividir las mitades
        merge_sort(izquierda)
        merge_sort(derecha)

        # Variables para fusionar las sublistas
        i = j = k = 0

        # Fusionar mientras haya elementos en ambas mitades
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arreglo[k] = izquierda[i]
                i += 1
            else:
                arreglo[k] = derecha[j]
                j += 1
            k += 1

        # Copiar los elementos restantes de la mitad izquierda
        while i < len(izquierda):
            arreglo[k] = izquierda[i]
            i += 1
            k += 1

        # Copiar los elementos restantes de la mitad derecha
        while j < len(derecha):
            arreglo[k] = derecha[j]
            j += 1
            k += 1

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
            print(f"Ordenando arreglo de tamaño {tamano} con Merge Sort...")
            inicio = time.time()
            merge_sort(arreglo)
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
