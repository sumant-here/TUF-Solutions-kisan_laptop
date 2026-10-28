class QueueStack:
    def __init__(self):
        self.qs = []

    def push(self, x):
        self.qs.append(x)
 

    def pop(self):
        if len(self.qs) == 0 :
            return -1
        return self.qs.pop()


    def top(self):
        if len(self.qs) == 0:
            return -1
        return self.qs[-1]
     

    def isEmpty(self):
        return len(self.qs) == 0 
