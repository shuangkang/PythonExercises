import math
class Distance(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def count_distance (self, Distance):
        return math.sqrt(abs(self.x - Distance.x)** 2 + abs(self.y - Distance.y) ** 2)

def main():
    distance = Distance(1, 2)
    print(distance.count_distance(Distance(1, 3)))
    print(distance.count_distance(Distance(2, 3)))

if __name__ == "__main__":
    main()