class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = 999999

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_ = val
        else:
            self.stack.append(val - self.min_)
            if val < self.min_:
                self.min_ = val
        

    def pop(self) -> None:
        if self.stack:
            value = self.stack.pop()
            if value < 0:
                self.min_ -= value

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min_
        else:
            return self.stack[-1] + self.min_

    def getMin(self) -> int:
        return self.min_