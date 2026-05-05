"""Merge Sort - Ordenamiento por mezcla."""


def sort(arr: list) -> list:
    """
    Ordena una lista usando el algoritmo Merge Sort.

    Complejidad: O(n log n) tiempo, O(n) espacio

    Args:
        arr: Lista de elementos comparables
        l: Índice izquierdo
        r: Índice derecho

    Returns:
        Lista ordenada
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left_slice = sort(arr[:mid])
    right_slice = sort(arr[mid:])

    return merge(left_slice, right_slice)

def merge(left: list, right: list) -> list:
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result