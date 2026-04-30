"""Tests para algoritmos de ordenamiento."""

import pytest
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


def generate_test_cases():
    """Casos de prueba comunes."""
    return [
        ([], []),
        ([1], [1]),
        ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([2, 2, 2, 2], [2, 2, 2, 2]),
        (["c", "b", "a"], ["a", "b", "c"]),
    ]


ALGORITHMS = [
    ("bubble", bubble_sort),
    ("selection", selection_sort),
    ("insertion", insertion_sort),
    ("merge", merge_sort),
    ("quick", quick_sort),
    ("heap", heap_sort),
    ("shell", shell_sort),
    ("radix", radix_sort),
    ("counting", counting_sort),
    ("bucket", bucket_sort),
    ("timsort", timsort),
]


@pytest.mark.parametrize("name,algorithm", ALGORITHMS)
def test_sort_empty(name, algorithm):
    """Test con lista vacía."""
    assert algorithm([]) == []


@pytest.mark.parametrize("name,algorithm", ALGORITHMS)
def test_sort_single(name, algorithm):
    """Test con un solo elemento."""
    assert algorithm([1]) == [1]


@pytest.mark.parametrize("name,algorithm", ALGORITHMS)
def test_sort_unordered(name, algorithm):
    """Test con lista desordenada."""
    assert algorithm([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]


@pytest.mark.parametrize("name,algorithm", ALGORITHMS)
def test_sort_reverse(name, algorithm):
    """Test con lista invertida."""
    assert algorithm([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("name,algorithm", ALGORITHMS)
def test_sort_already_sorted(name, algorithm):
    """Test con lista ya ordenada."""
    assert algorithm([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("name,algorithm", ALGORITHMS)
def test_sort_duplicates(name, algorithm):
    """Test con elementos duplicados."""
    assert algorithm([2, 2, 2, 2]) == [2, 2, 2, 2]