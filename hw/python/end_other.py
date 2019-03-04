#!/usr/bin/python3
def end_other(a, b):
  suff = min(len(a), len(b))
  return a[-suff:].lower() == b[-suff:].lower()

def assert_eq(a, b):
  print(f"\tAct:{a}==Exp:{b}")
  assert(a == b)

def test():
  print(f"Test ({__file__}):")

  assert_eq(end_other('Hiabc', 'bc'), True)
  assert_eq(end_other('ab', 'ab12'), False)
  assert_eq(end_other('AbC', 'HiaBc'), True)
  assert_eq(end_other('ab', '12ab'), True)

  print(f"\tTests success.")

if __name__ == "__main__":
  test()