class MinStack:

    def __init__(self):
        self.base = []
        

    def push(self, val: int) -> None:
        self.base.append(val)

    def pop(self) -> None:
        if self.base:
            self.base.pop()

    def top(self) -> int:
        return self.base[-1] if self.base else None

    def getMin(self) -> int:
        return min(self.base) if self.base else None
        
