class MyHashSet:

    def __init__(self):
        self.base = {}
        

    def add(self, key: int) -> None:
        self.base[key] = 1
        

    def remove(self, key: int) -> None:
        if key in self.base:
            del self.base[key]
        

    def contains(self, key: int) -> bool:
        return key in self.base
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)