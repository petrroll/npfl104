def end_other(a, b):
  suff = min(len(a), len(b))
  return a[-suff:].lower() == b[-suff:].lower()

def test():
  assert(end_other('Hiabc', 'bc') == True)
  assert(end_other('ab', 'ab12') == False)
  assert(end_other('AbC', 'HiaBc') == True)
  assert(end_other('ab', '12ab') == True)

  print(f"Test ({__file__}) success.")

if __name__ == "__main__":
  test()