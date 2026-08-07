"""Utility: calculate statistics for a 3x3 matrix from 9 numbers."""

from typing import List, Dict, Any
import numpy as np


def calculate(list_of_numbers: List[float]) -> Dict[str, Any]:
    """Return a dictionary with mean, standard deviation, variance, max, min and sum.

    The values are lists: [axis0, axis1, flattened]
    """
    if len(list_of_numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.array(list_of_numbers).reshape(3, 3)
    calculations = {
        'mean': [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()],
        'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()],
        'variance': [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()],
        'max': [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).tolist()],
        'min': [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).tolist()],
        'sum': [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()],
    }
    return calculations


if __name__ == '__main__':
    # quick smoke test
    example = list(range(9))
    print(calculate(example))

calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])