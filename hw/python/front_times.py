def front_times(str, n):
  return str[:3]*n

def test():
    assert(front_times('Chocolate', 2) == "ChoCho")
    assert(front_times('Chocolate', 3) == "ChoChoCho")
    assert(front_times('', 3) == "")
    assert(front_times('Chocolate', 0) == "")
    assert(front_times('Ab', 3) == "AbAbAb")
    print(f"Test ({__file__}) success.")


if __name__ == "__main__":
    test()