from random import randrange


N = int(raw_input("Podaj ile liczba w tablicy : "))


list = []
for i in range(N):
  i = randrange(1,N)	  
  list.append(i)

def quick(list,counter=0):
  if list == []:
    return []
  else:
    pivot = list[0]
    
    L = quick([x for x in list[1:] if x < pivot])
    R = quick([x for x in list[1:]  if x >= pivot])
    
    counter = counter + 1
    

    return L + [pivot] + R
  
d = list   
print "Przed posortowaniem : \n", d,"\n" 
g = quick(d)
print "Po posortowaniu : \n",  g,"\n"
