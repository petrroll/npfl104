#!/usr/bin/python3
def count_evens(nums):
  return sum([1 for x in nums if x % 2 == 0])
  
def assert_eq(a, b):
  print(f"\tAct:{a}==Exp:{b}")
  assert(a == b)

def test():
  print(f"Test ({__file__}):")

  assert_eq(count_evens([2, 2, 0]), 3)
  assert_eq(count_evens([1, 3, 5]), 0)

  print(f"\tTests success.")

if __name__ == "__main__":
  test()