def count_hi(str):
  return str.count("hi")

def test():
    assert(count_hi('') == 0)
    assert(count_hi('hsi') == 0)
    assert(count_hi('hi') == 1)
    assert(count_hi('hihiqhi') == 3)

    print(f"Test ({__file__}) success.")


if __name__ == "__main__":
    test()