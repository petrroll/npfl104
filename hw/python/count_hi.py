#!/usr/bin/python3
def count_hi(str):
  return str.count("hi")

def assert_eq(a, b):
  print(f"\tAct:{a}==Exp:{b}")
  assert(a == b)

def test():
  print(f"Test ({__file__}):")
  assert_eq(count_hi(''), 0)
  assert_eq(count_hi('hsi'), 0)
  assert_eq(count_hi('hi'), 1)
  assert_eq(count_hi('hihiqhi'), 3)
  print(f"\tTests success.")


if __name__ == "__main__":
  test()