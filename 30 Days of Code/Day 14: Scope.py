class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        self.__elements.sort()
        self.maximumDifference = self.__elements[len(self.__elements)-1] - self.__elements[0]

    



# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference
