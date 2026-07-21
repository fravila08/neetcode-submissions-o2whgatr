class MyQueue:

    def __init__(self):
        self.base = []

    def push(self, x: int) -> None:
        self.base.insert(0, x)

    def pop(self) -> int:
        return None if self.empty() else self.base.pop()
        
    def peek(self) -> int:
        return None if self.empty() else self.base[-1]

    def empty(self) -> bool:
        return not self.base
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()