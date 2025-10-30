# python
def mean_of_three(a: float, b: float, c: float) -> float:
    """Return the arithmetic mean of three numeric values. Raises TypeError for non-numbers."""
    for x in (a, b, c):
        if not isinstance(x, (int, float)):
            raise TypeError(f"All arguments must be numbers, got {type(x).__name__}")
    return (a + b + c) / 3.0

# Examples
if __name__ == "__main__":
    print(mean_of_three(1, 2, 3))      # 2.0
    print(mean_of_three(4.5, 5.5, 6.0))# 5.333333333333333