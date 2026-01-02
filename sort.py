def sort(width, height, length, mass):
  """
  Dispatch a package to the correct stack based on its dimensions and mass.
  Parameters:
  width (int or float): cm
  height (int or float): cm
  length (int or float): cm
  mass (int or float): kg
  Returns:
  str: 'STANDARD', 'STANDARD', 'SPECIAL', or 'REJECTED'
  """
  volume = width * height * length

is bulky = (
  volume >= 1_000_000 or 
  width >= 150 or
  height >= 150 or 
  length >= 150
)
is heavy = mass >= 20 

return ( 
"REJECTED" if is_bulky and is_heavy
  else "SPECIAL" if is_bulky or is_heavy
  else "STANDARD"
)

if __name__== "__main__":
  test_cases = [
    (100, 100, 100, 10, "STANDARD"),
    (100, 100, 100, 25, "REJECTED"),
    (150, 50, 50, 10, "SPECIAL"),
    (50, 50, 50, 20, "SPECIAL"),
    (200, 200, 50, 30, "REJECTED'),
     ]
  for w, h, l, m, expected in test_cases:
    result = sort w, h, l, m)
    print (f"sort({w}, {h}. {l}, {m}) -> {result} | Expected : {expected}") 
