#!/usr/bin/python3
def xyz_there(str):
  return str.count(".xyz") < str.count("xyz")

def assert_eq(a, b):
  print(f"\tAct:{a}==Exp:{b}")
  assert(a == b)

def test():
  print(f"Test ({__file__}):")
  assert_eq(xyz_there('xyz.abc'), True)
  assert_eq(xyz_there('abc.xyzxyz'), True)
  assert_eq(xyz_there('12.xyz'), False)
  print(f"\tTests success.")


if __name__ == "__main__":
  test()