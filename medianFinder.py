class MedianFinder:

    def __init__(self):
        self.arr = []
        self.n = 0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        self.n += 1

    def findMedian(self) -> float:
        if self.n % 2 == 1:
            return self.arr[self.n//2]
        else:
            return (self.arr[self.n//2] + self.arr[self.n//2 - 1])/2
