#!/usr/bin/python3
def front_times(str, n):
  return str[:3]*n

def assert_eq(a, b):
  print(f"\tAct:{a}==Exp:{b}")
  assert(a == b)


def test():
  print(f"Test ({__file__}):")
  assert_eq(front_times('Chocolate', 2), "ChoCho")
  assert_eq(front_times('Chocolate', 3), "ChoChoCho")
  assert_eq(front_times('', 3), "")
  assert_eq(front_times('Chocolate', 0), "")
  assert_eq(front_times('Ab', 3), "AbAbAb")
  print(f"\tTests success.")


if __name__ == "__main__":
    test()