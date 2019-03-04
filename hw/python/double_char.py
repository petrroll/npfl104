#!/usr/bin/python3
def double_char(str):
  return "".join([x+x for x in str])

def assert_eq(a, b):
  print(f"\tAct:{a}==Exp:{b}")
  assert(a == b)

def test():
  print(f"Test ({__file__}):")
  assert_eq(double_char("The"), 'TThhee')
  assert_eq(double_char("Hi-There"), 'HHii--TThheerree')
  assert_eq(double_char(""), '')
  print(f"\tTests success.")


if __name__ == "__main__":
    test()