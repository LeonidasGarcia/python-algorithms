# Python Algorithms

Colección de algoritmos de ordenamiento implementados en Python.

## Algoritmos incluidos

| Algoritmo | Complejidad Temporal | Complejidad Espacial |
|-----------|---------------------|---------------------|
| Bubble Sort | O(n²) | O(1) |
| Selection Sort | O(n²) | O(1) |
| Insertion Sort | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n) |
| Quick Sort | O(n log n) promedio | O(log n) |
| Heap Sort | O(n log n) | O(1) |
| Shell Sort | O(n^(3/2)) promedio | O(1) |
| Radix Sort | O(nk) | O(n+k) |
| Counting Sort | O(n + k) | O(k) |
| Bucket Sort | O(n + k) promedio | O(k) |
| Timsort | O(n log n) | O(n) |

## Instalación

```bash
uv sync
```

## Desarrollo

```bash
# Instalar dependencias de desarrollo
uv sync --extra dev

# Ejecutar tests
uv run pytest

# Ejecutar benchmarks
uv run python benchmarks/benchmark.py
```

## Estructura

```
src/sorting/
├── __init__.py    # Exports de todos los algoritmos
├── bubble.py      # Bubble Sort
├── selection.py   # Selection Sort
├── insertion.py   # Insertion Sort
├── merge.py       # Merge Sort
├── quick.py       # Quick Sort
├── heap.py        # Heap Sort
├── shell.py       # Shell Sort
├── radix.py       # Radix Sort
├── counting.py    # Counting Sort
├── bucket.py      # Bucket Sort
└── timsort.py     # Timsort
```