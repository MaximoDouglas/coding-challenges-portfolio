def nth_fib(n):
  if (n == 1):
      return 0
  
  f = [0, 1, 1]
  for i in range(3, n):
      f.append(f[i - 1] + f[i - 2])
  
  return f[n - 1]