#!/usr/bin/python3
def array_count9(nums):
  return nums.count(9)

def assert_eq(a, b):
  print(f"\tAct:{a}==Exp:{b}")
  assert(a == b)

def test():
  print(f"Test ({__file__}):")
  assert_eq(array_count9([1, 2, 9]), 1)
  assert_eq(array_count9([9, 3, 2, 9]), 2)
  assert_eq(array_count9([]), 0)
  print(f"\tTests success.")


if __name__ == "__main__":
  test()