class MinStack:

    def __init__(self):
        self.mini = None
        self.base = []
        self.mini_rec = []  

    def push(self, val: int) -> None:
        if self.mini is None or val <= self.mini :
            self.mini = val
            self.mini_rec.append(val)
        print(self.mini_rec)
        self.base.append(val)

    def pop(self) -> None:
        if self.top() == self.mini:
            self.mini_rec.pop()
            self.mini = self.mini_rec[-1] if self.mini_rec else None
        print(self.mini_rec)
        self.base.pop(-1) if self.base else None

    def top(self) -> int:
        return self.base[-1] if self.base else None

    def getMin(self) -> int:
        return self.mini
        
