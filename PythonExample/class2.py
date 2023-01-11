class Sample:
    counter2 = 0# 모든 객체를 통틀어서 하나만 존재(전역변수)
    def __init__(self):
        self.counter = 0# 해당 객체 전체에서 사용가능, 하지만 해당 객체에서만 사용가능 (공유 x)(지역변수)
    def numEven(self, n):
        for k in range(n):
            if k % 2 ==0:
                self.counter +=1
                Sample.counter2 +=1
    def __not_used(self):
        print("hi")


s1 = Sample()
s2 = Sample()

s1.numEven(15)
s2.numEven(15)
#s1.__not_used() : __이 붙어서 호출안됨.
print(s1.counter,s2.counter2)