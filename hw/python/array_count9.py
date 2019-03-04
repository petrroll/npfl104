def array_count9(nums):
  return nums.count(9)


def test():
    assert(array_count9([1, 2, 9]) == 1)
    assert(array_count9([9, 3, 2, 9]) == 2)
    assert(array_count9([]) == 0)
    print(f"Test ({__file__}) success.")


if __name__ == "__main__":
    test()