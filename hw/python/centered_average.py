#!/usr/bin/python3
def centered_average(nums):
  if len(nums) <= 2: return 0
  return (sum(nums) - min(nums) - max(nums)) / (len(nums) - 2)  

def assert_eq(a, b):
  print(f"\tAct:{a}==Exp:{b}")
  assert(a == b)

def test():
  print(f"Test ({__file__}):")
  assert_eq(centered_average([1, 7, 8]), 7)
  assert_eq(centered_average([4, 4, 4, 4, 5]), 4)
  assert_eq(centered_average([1, 8]), 0)
  print(f"\tTests success.")


if __name__ == "__main__":
  test()