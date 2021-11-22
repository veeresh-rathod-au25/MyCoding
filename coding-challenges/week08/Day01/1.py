class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(val, self.min)

    def pop(self) -> None:
        if self.stack.pop(-1) == self.min:
            self.min = min(self.stack) if self.stack else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min