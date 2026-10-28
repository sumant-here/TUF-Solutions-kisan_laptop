class ArrayStack:
    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)
 

    def pop(self):
        if len(self.arr) == 0 :
            return -1
        return self.arr.pop()


    def top(self):
        if len(self.arr) == 0 :
            return -1
        return self.arr[-1]
     

    def isEmpty(self):
        return len(self.arr) == 0 
