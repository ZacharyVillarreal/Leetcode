class OrderedStream:

    def __init__(self, n: int):
        self.data = [None] * n
        self.point = 0

    def insert(self, id: int, value: str) -> List[str]:
        # Need to deal with the problem that the id index starts at 1 when it should be 0
        id -= 1
        self.data[id] = value
        if id > self.point:
            return []
        while self.point < len(self.data) and self.data[self.point]:
            self.point += 1
            
        return self.data[id : self.point]
            


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)