#!/usr/bin/python3
def string_match(a, b):
  count = 0
  for i in range(min(len(a), len(b)) - 1):
    if a[i:i+2] == b[i:i+2]: count += 1
  return count

def assert_eq(a, b):
  print(f"\tAct:{a}==Exp:{b}")
  assert(a == b)

def test():
  print(f"Test ({__file__}):")
  assert_eq(string_match('abc', 'abc'), 2)
  assert_eq(string_match('abc', 'axc'), 0)
  assert_eq(string_match('iaxxai', 'aaxxaaxx'), 3)
  assert_eq(string_match('', 'aaxxaaxx'), 0)
  print(f"\tTests success.")


if __name__ == "__main__":
    test()