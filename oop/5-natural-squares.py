class NaturalSquares:
    def __init__(self, n):
        self.current = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration

 
# Test Case 1
squares = NaturalSquares(5)
assert list(squares) == [1, 4, 9, 16, 25]

# Test Case 2
squares = NaturalSquares(10)
assert list(squares) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Test Case 3
squares = NaturalSquares(0)
assert list(squares) == []
