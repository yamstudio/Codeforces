input()
l = map(int, raw_input().split())
prev = 0
m = 0
n = 0
for i in l:
  if i >= prev:
    n += 1
    m = max(m, n)
  else:
    n = 1
  prev = i
print max(m, n)
