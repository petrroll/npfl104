def big_diff(nums):
  if not nums: return 0
  return max(nums) - min(nums)
  
def test():
  assert(big_diff([10, 3, 5, 6]) == 7)
  assert(big_diff([10]) == 0)
  assert(big_diff([10, 10]) == 0)
  assert(big_diff([]) == 0)

  print(f"Test ({__file__}) success.")


if __name__ == "__main__":
  test()