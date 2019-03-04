def string_match(a, b):
  count = 0
  for i in range(min(len(a), len(b)) - 1):
    if a[i:i+2] == b[i:i+2]: count += 1
  return count



def test():
    assert(string_match('abc', 'abc') == 2)
    assert(string_match('abc', 'axc') == 0)
    assert(string_match('iaxxai', 'aaxxaaxx') == 3)
    assert(string_match('', 'aaxxaaxx') == 0)

    print(f"Test ({__file__}) success.")


if __name__ == "__main__":
    test()