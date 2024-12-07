
with open('input', 'r') as f:
    data = f.read().strip().splitlines()

ops = '+*'

total = 0
for line in data:
    target, rest = line.split(':')
    target = int(target)
    values = map(int, rest.strip().split(' '))
    start = next(values)
    poss = [ start ]
    for i in values:
        poss_new = []
        for op in ops:
            for j in poss:
                e = eval(f'{j} {op} {i}')
                poss_new.append(e)
        poss = poss_new

    if target in poss:
        total += target

print(total)


ops = '+*|'

total = 0
for line in data:
    target, rest = line.split(':')
    target = int(target)
    values = map(int, rest.strip().split(' '))
    start = next(values)
    poss = [ start ]
    for i in values:
        poss_new = []
        for op in ops:
            for j in poss:
                if op == '|':
                    e = int(eval(f'str({j}) + str({i})'))
                else:
                    e = eval(f'{j} {op} {i}')

                poss_new.append(e)
        poss = poss_new

    if target in poss:
        total += target

print(total)

# 7710205485870
# 20928985450275
# (130 seconds :sob:)
