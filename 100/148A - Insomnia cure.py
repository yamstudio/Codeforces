x = []
d = 0
for _ in range(4):
  x.append(int(raw_input()))
for i in range(input()):
  if any(((i + 1) % j == 0) for j in x):
    d += 1
print d
