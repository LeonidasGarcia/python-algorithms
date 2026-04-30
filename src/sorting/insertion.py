"""Insertion Sort - Ordenamiento por inserción."""


def sort(arr: list) -> list:
    """
    Ordena una lista usando el algoritmo Insertion Sort.

    Complejidad: O(n^2) tiempo, O(1) espacio

    Args:
        arr: Lista de elementos comparables

    Returns:
        Lista ordenada
    """
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
