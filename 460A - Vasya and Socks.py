n, m = map(int, raw_input().split())
p = n
e = p
while e >= m:
  p += e / m
  e = e / m + e % m
print p
