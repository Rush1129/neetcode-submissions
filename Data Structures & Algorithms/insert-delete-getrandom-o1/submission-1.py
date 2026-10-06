class RandomizedSet:

    def __init__(self):
        self.rhash = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val not in self.rhash:
            self.rhash[val]=len(self.l)
            self.l.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.rhash:
            idx = self.rhash[val]
            last = self.l[-1]
            self.l[idx] = last
            self.rhash[last] = idx
            self.l.pop()
            del self.rhash[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()