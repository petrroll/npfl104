#!/usr/bin/python3
def big_diff(nums):
  if not nums: return 0
  return max(nums) - min(nums)
  
def assert_eq(a, b):
  assert(a == b)
  print(f"\tAct:{a}==Exp:{b}")

def test():
  print(f"Test ({__file__}):")
  assert_eq(big_diff([10, 3, 5, 6]), 7)
  assert_eq(big_diff([10]), 0)
  assert_eq(big_diff([10, 10]), 0)
  assert_eq(big_diff([]), 0)
  print(f"\tTests success.")

if __name__ == "__main__":
  test()