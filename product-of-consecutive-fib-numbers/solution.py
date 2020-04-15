fib = {0: 0, 1: 1}

def F(m):
    if(m in fib):
      return fib[m]
    else:
      fib[m] = F(m-1) + F(m-2)
      return fib[m]

def productFib(prod):
    for i in range(prod + 1):
      fj = F(i+1)
      fi = F(i)

      if (fi * fj == prod):
        return [fi, fj, True]
      elif (fi * fj > prod):
        return [fi, fj, False]