
with open('input', 'r') as f:
    data = f.read().strip()

# mul(x,y) where x y integers

count = 0
for mul in data.split('mul('):
    commas = mul.split(',')
    try: lhs, rhs = map(int, (commas[0], commas[1].split(')')[0]))
    except (IndexError, ValueError): continue
    count += lhs * rhs

print(count)


count = 0
enabled = True
for mul in data.split('mul('):
    was_enabled = enabled

    if "don't()" in mul: enabled = False
    if 'do()' in mul: enabled = True
    if not was_enabled: continue

    commas = mul.split(',')
    try: lhs, rhs = map(int, (commas[0], commas[1].split(')')[0]))
    except (IndexError, ValueError): continue
    count += lhs * rhs

print(count)
