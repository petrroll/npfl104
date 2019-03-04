def count_evens(nums):
  return sum([1 for x in nums if x % 2 == 0])
  
def test():
  assert(count_evens([2, 2, 0]) == 3)
  assert(count_evens([1, 3, 5]) == 0)

  print(f"Test ({__file__}) success.")

if __name__ == "__main__":
  test()