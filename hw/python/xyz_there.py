def xyz_there(str):
  return str.count(".xyz") < str.count("xyz")
  
def test():
  assert(xyz_there('xyz.abc') == True)
  assert(xyz_there('abc.xyzxyz') == True)
  assert(xyz_there('12.xyz') == False)

  print(f"Test ({__file__}) success.")


if __name__ == "__main__":
  test()