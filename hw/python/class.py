#!/usr/bin/python3
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def Abs(self):
        return (self.x ** 2 + self.y ** 2) ** (1/2)

def assert_eq(a, b):
  print(f"\tAct:{a}==Exp:{b}")
  assert(a == b)


def test():
  print(f"Test ({__file__}):")
  
  a = Point(3, 4)
  assert_eq(a.Abs(), 5)
  assert_eq((a + a).x, 6)  
  
  print(f"\tTests success.")


if __name__ == "__main__":
  test()