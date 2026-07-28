# dict[key], set[val], lst[idx]

class MinStack:

    def __init__(self):
        self.base = []
        self.min_val = []

    def push(self, val: int) -> None:
        if not self.min_val or self.getMin() >= val:
            self.min_val.append(val)
        self.base.append(val)

    def pop(self) -> None:
        if self.top() == self.getMin():
            self.min_val.pop()
        if self.base: 
            self.base.pop()

    def top(self) -> int:
        return self.base[-1] if self.base else None

    def getMin(self) -> int:
        return self.min_val[-1] if self.min_val else None
        
