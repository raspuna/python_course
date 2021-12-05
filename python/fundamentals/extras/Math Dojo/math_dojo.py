import math

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self


if __name__ == "__main__" :
    # create an instance:
    md = MathDojo()
    # to test:
    x = md.add(2).add(2,5,1).subtract(3,2).result
    print(x)	# should print 5
    # run each of the methods a few more times and check the result!

    md2 = MathDojo()
    y = md2.add(pow(2, 32), pow(2, 32)).result
    print(y)

    md3 = MathDojo()
    z = md3.add(7,14,21,28,35).add(1,2,3,4,5,6,7,8,9,10).add(9,7,5,3,1).result
    print(z)
    z2 = 7+14+21+28+35+55+25
    if z != z2:
        print("wrong")
    
    z = md3.subtract(55).subtract(10,8,6,4,2).subtract(7,14,21,28).result
    z3 = z2 - 55 - 30 - 70
    print(z)
    if z != z3:
        print("wrong")

