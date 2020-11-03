class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.numBig = big
        self.numMedium = medium
        self.numSmall = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.numBig >= 1:
                self.numBig -= 1
                return True
            return False
        elif carType == 2:
            if self.numMedium >= 1:
                self.numMedium -= 1
                return True
            return False
        if self.numSmall >= 1:
            self.numSmall -= 1
            return True
        return False
