#!/usr/bin/python3
def string_splosion(str):
  return "".join([str[:i] for i in range(len(str)+1)])
  
def assert_eq(a, b):
  print(f"\tAct:{a}==Exp:{b}")
  assert(a == b)

def test():
  print(f"Test ({__file__}):")
  assert_eq(string_splosion('Code'), 'CCoCodCode')
  assert_eq(string_splosion('x'), 'x')
  assert_eq(string_splosion(''), '')
  print(f"\tTests success.")


if __name__ == "__main__":
  test()