l = [0] * 3
for _ in range(input()):
  l = [x + y for x, y in zip(l, map(int, raw_input().split()))]
print ['NO', 'YES'][l == [0] * 3]
