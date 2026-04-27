class MyHashMap:

    def __init__(self, name=None):
        self.base = {}
        self.name = name
        
    def put(self, key: int, value: int) -> None:
        self.base[key] = value
        
    def get(self, key: int) -> int:
        return self.base.get(key, -1)

    def remove(self, key: int) -> None:
        if self.base.get(key):
            del self.base[key] 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)