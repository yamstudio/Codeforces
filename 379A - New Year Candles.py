a, b = map(int, raw_input().split())
t = 0
while a >= b:
  a -= (b - 1)
  t += b
t += a
print t
