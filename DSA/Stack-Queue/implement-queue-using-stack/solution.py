class StackQueue:
    def __init__(self):
        self.sq = []

    def push(self, x):
        self.sq.append(x)
 

    def pop(self):
        if len(self.sq) == 0:
            return -1
        return self.sq.pop(0)


    def peek(self):
        if len(self.sq) ==0:
            return -1
        return self.sq[0]
     

    def isEmpty(self):
        return len(self.sq) == 0
