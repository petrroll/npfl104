def double_char(str):
  return "".join([x+x for x in str])

def test():
  assert(double_char("The") == 'TThhee')
  assert(double_char("Hi-There") == 'HHii--TThheerree')
  assert(double_char("") == '')

  print(f"Test ({__file__}) success.")


if __name__ == "__main__":
    test()