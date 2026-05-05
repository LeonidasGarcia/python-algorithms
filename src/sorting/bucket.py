"""Bucket Sort - Ordenamiento por cubetas."""

def insertion_sort(arr: list) -> list:
    left = 0
    right = len(arr) - 1

    for i in range(left + 1, right + 1):
        temp = arr[i]
        j = i - 1

        while j >= left and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

    return arr

def sort(arr: list, bucket_size: int = 5) -> list:
    """
    Ordena una lista usando el algoritmo Bucket Sort.

    Complejidad: O(n + k) tiempo promedio, O(k) espacio

    Args:
        arr: Lista de elementos comparables
        bucket_size: Tamaño de cada cubeta

    Returns:
        Lista ordenada
    """
    if not arr: return arr

    min_val, max_val = min(arr), max(arr)

    if min_val is max_val: return arr
    
    num_buckets = (((max_val - min_val) // bucket_size) + 1)
    buckets = [[] for _ in range(num_buckets)] 

    for num in arr:
        bucket_index = (num - min_val) // bucket_size
        buckets[bucket_index].append(num)
    
    sorted_array = []

    for bucket in buckets:
        insertion_sort(bucket)
        sorted_array.extend(bucket)
    
    return sorted_array