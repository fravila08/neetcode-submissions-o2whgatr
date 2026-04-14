class MinStack:

    def __init__(self):
        self.base = []
        self.mini_rec = []  

    def push(self, val: int) -> None:
        if not self.mini_rec or val <= self.mini_rec[-1] :
            self.mini_rec.append(val)
        self.base.append(val)

    def pop(self) -> None:
        if self.top() == self.mini_rec[-1]:
            self.mini_rec.pop()
        self.base.pop(-1) if self.base else None

    def top(self) -> int:
        return self.base[-1] if self.base else None

    def getMin(self) -> int:
        return self.mini_rec[-1]
        
