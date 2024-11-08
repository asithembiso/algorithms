"""
 Test Binary Search function
"""

from binary_search import binary_search
import pytest


@pytest.mark.parametrize("arr, target, expected", [
    ([1, 3, 4, 7, 9, 13, 15, 19, 21], 7, 3),
    ([1, 3, 4, 7, 9, 13, 15, 19, 21], 9, 4),
    ([1, 3, 4, 7, 9, 13, 15, 19, 21], 21, 8),
    ([1, 3, 4, 7, 9, 13, 15, 19, 21], 0, -1),
    ([1, 3, 4, 7, 9, 13, 15, 19, 21], 22, -1),
    ([], 7, -1),
    ([1], 1, 0),
    ([1], 2, -1)
])
def test_binary_search(arr, target, expected):
    assert binary_search(arr, target) == expected
