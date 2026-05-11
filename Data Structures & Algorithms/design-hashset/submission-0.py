class MyHashSet:

    hasht = []
    def __init__(self):
        self.hasht = []
        

    def add(self, key: int) -> None:
        if key not in self.hasht:
            self.hasht.append(key)

    def remove(self, key: int) -> None:
        if key in self.hasht:
            self.hasht.remove(key)    

    def contains(self, key: int) -> bool:
        if key in self.hasht:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)