
with open('input', 'r') as f:
    data = f.read().strip().splitlines()

lefts = []
rights = []

for line in data:
    l, r = map(int, line.split('   '))
    lefts.append(l)
    rights.append(r)

# part 1
print(sum(abs(l - r)
          for l, r in zip(sorted(lefts), sorted(rights))))

# part 2
print(sum(l * rights.count(l)
          for l in lefts))
