from random import randrange


N = raw_input("Podaj ile liczba w tablicy : ")

def convert(n):
  try:
    ret = int(n)
  except ValueError:
    ret = float(n)
  return ret
N = convert(N)  
    
list = []
for i in range(N):
  i = randrange(1,N)	  
  list.append(i)
#print Temp

def quick(list):
  if list == []:
    return []
  else:
    pivot = list[0]
    L = quick([x for x in list[1:] if x < pivot])
    R = quick([x for x in list[1:] if x >= pivot])
    
    return L + [pivot] + R

d = list   
print "Przed posortowaniem : ", d, #len(d)
g = quick(d)
print "Po posortowaniu : ",  g, # len(g)