"""Bubble Sort - Ordenamiento de burbuja."""


def sort(arr: list) -> list:
    """
    Ordena una lista usando el algoritmo Bubble Sort.

    Complejidad: O(n^2) tiempo, O(1) espacio

    Args:
        arr: Lista de elementos comparables

    Returns:
        Lista ordenada
    """

    if len(arr) == 1:
        return arr

    for i in range(len(arr)):
        is_swapped = False

        for j in range(1, (len(arr)) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                is_swapped = True

        if not is_swapped:
            break

    return arr
