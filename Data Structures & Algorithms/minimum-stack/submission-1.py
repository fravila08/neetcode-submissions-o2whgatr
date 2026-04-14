class MinStack:

    def __init__(self):
        self.base = []
        

    def push(self, val: int) -> None:
        self.base.append(val)
        

    def pop(self) -> None:
        self.base.pop(-1) if self.base else None

    def top(self) -> int:
        return self.base[-1] if self.base else None

    def getMin(self) -> int:
        return min(self.base)
        
