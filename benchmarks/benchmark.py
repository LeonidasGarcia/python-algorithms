"""Benchmark para comparar algoritmos de ordenamiento."""

import time
import random
from typing import Callable, Any

from src.sorting import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort,
    shell_sort,
    radix_sort,
    counting_sort,
    bucket_sort,
    timsort,
)


def benchmark(algorithm: Callable, arr: list, runs: int = 100) -> dict:
    """
    Mide el rendimiento de un algoritmo.

    Args:
        algorithm: Función de ordenamiento
        arr: Lista a ordenar
        runs: Número de ejecuciones

    Returns:
        Diccionario con estadísticas
    """
    times = []
    result = None

    for _ in range(runs):
        test_arr = arr.copy()
        start = time.perf_counter()
        result = algorithm(test_arr)
        end = time.perf_counter()
        times.append(end - start)

    return {
        "min": min(times),
        "max": max(times),
        "avg": sum(times) / len(times),
        "result": result,
    }


def run_benchmarks(sizes: list[int] = None) -> None:
    """Ejecuta todos los benchmarks."""
    if sizes is None:
        sizes = [100, 500, 1000, 5000]

    algorithms = [
        ("bubble_sort", bubble_sort),
        ("selection_sort", selection_sort),
        ("insertion_sort", insertion_sort),
        ("merge_sort", merge_sort),
        ("quick_sort", quick_sort),
        ("heap_sort", heap_sort),
        ("shell_sort", shell_sort),
        ("radix_sort", radix_sort),
        ("counting_sort", counting_sort),
        ("bucket_sort", bucket_sort),
        ("timsort", timsort),
    ]

    print("=" * 80)
    print("BENCHMARK DE ALGORITMOS DE ORDENAMIENTO")
    print("=" * 80)

    for size in sizes:
        print(f"\n--- Tamaño: {size} ---")
        arr = [random.randint(0, 10000) for _ in range(size)]

        for name, algorithm in algorithms:
            try:
                result = benchmark(algorithm, arr, runs=10)
                print(f"{name:20s} | avg: {result['avg']*1000:8.2f}ms | min: {result['min']*1000:8.2f}ms")
            except Exception as e:
                print(f"{name:20s} | ERROR: {e}")


def plot_results(results: dict) -> None:
    """Genera gráfico de resultados (requiere matplotlib)."""
    try:
        import matplotlib.pyplot as plt
        import numpy as np

        sizes = list(results.keys())
        algorithms = list(next(iter(results.values())).keys())

        fig, ax = plt.subplots(figsize=(12, 6))

        for algo in algorithms:
            times = [results[size][algo]["avg"] * 1000 for size in sizes]
            ax.plot(sizes, times, marker="o", label=algo)

        ax.set_xlabel("Tamaño del array")
        ax.set_ylabel("Tiempo promedio (ms)")
        ax.set_title("Comparación de Algoritmos de Ordenamiento")
        ax.legend()
        ax.grid(True)
        plt.tight_layout()
        plt.show()

    except ImportError:
        print("matplotlib no disponible. Instala con: uv add benchmark matplotlib numpy")


if __name__ == "__main__":
    run_benchmarks()