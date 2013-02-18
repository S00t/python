# 1 + 1/n

def gen(n):
  i = 1.00
  counter = 0
  while i <= n:
    if i != n :
      i = i + (1/(i+1))
      counter = counter + 1
  yield i, counter

  
d = gen(5)
f = gen(10)
print "dla 5: ",next(d)
print "dla 10: ",next(f)
