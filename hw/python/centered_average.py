def centered_average(nums):
  if len(nums) <= 2: return 0
  return (sum(nums) - min(nums) - max(nums)) / (len(nums) - 2)  

def test():
  assert(centered_average([1, 7, 8]) == 7)
  assert(centered_average([4, 4, 4, 4, 5]) == 4)
  assert(centered_average([1, 8]) == 0)
  
  print(f"Test ({__file__}) success.")


if __name__ == "__main__":
  test()