def string_splosion(str):
  return "".join([str[:i] for i in range(len(str)+1)])
  
def test():
  assert(string_splosion('Code') == 'CCoCodCode')
  assert(string_splosion('x') == 'x')
  assert(string_splosion('') == '')


  print(f"Test ({__file__}) success.")


if __name__ == "__main__":
  test()