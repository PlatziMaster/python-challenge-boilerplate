"""Solution by pablotrinidad."""


class Solution:
    """Solution to the Fibonacci problem."""

    def __init__(self):
        self.mem = [0, 1]

    def fib(self, i: int) -> int:
        """Returns the i-th fibonacci number."""
        if i < len(self.mem):
            return self.mem[i-1]
        r = self.fib(i-1) + self.fib(i-2)
        self.mem.append(r)
        return r
