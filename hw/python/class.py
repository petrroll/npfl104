class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def Abs(self):
        return (self.x ** 2 + self.y ** 2) ** 1/2


def test():
  a = Point(1, 1)
  assert(a.Abs() == 1)

  assert((a + a).x == 2)  
  print(f"Test ({__file__}) success.")


if __name__ == "__main__":
  test()