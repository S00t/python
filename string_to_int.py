N = raw_input("Podaj ile liczba w tablicy : ")

def convert(n):
  try:
    ret = int(n)
  except ValueError:
    ret = float(n)
  return ret
N = convert(N)  
    