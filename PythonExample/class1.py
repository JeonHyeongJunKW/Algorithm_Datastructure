class Sample:
    def __init__(self):
        self.counter=0
    def numEven(self, n):
        for k in range(n):
            if k % 2 ==0:
                self.counter +=1
        return self.counter


s= Sample()
print("# of even integers =",s.numEven(15))