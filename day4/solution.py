
with open('input', 'r') as f:
    data = f.read().strip().splitlines()

directions = ((0, 1), (0, -1), (1, 0), (-1, 0),
              (1, 1), (-1, 1), (1, -1), (-1, -1))

def add(t1, t2):
    return tuple(map(sum, zip(t1, t2)))

def at(row, col, data=data):
    if (row, col) != clamp(row, col): return ''
    else: row, col = clamp(row, col)
    return data[row][col]

def clamp(row, col, data=data):
    row_hi = len(data) - 1
    col_hi = len(data[0]) - 1

    return (max(min(row, row_hi), 0), max(min(col, col_hi), 0))

count = 0
for direction in directions:
    for row in range(len(data)):
        for col in range(len(data[row])):
            x = at(row, col)
            m = at(*add((row, col), direction))
            a = at(*add((row, col), add(direction, direction)))
            s = at(*add((row, col), add(direction, add(direction, direction))))

            xmas = ''.join((x, m, a, s))
            if xmas == 'XMAS':
                count += 1

print(count)


count = 0
directions = (((1, 1), (-1, -1)), ((-1, 1), (1, -1)))
for row in range(len(data)):
    for col in range(len(data[row])):
        a = at(row, col)
        m1 = at(*add((row, col), directions[0][0]))
        s1 = at(*add((row, col), directions[0][1]))
        m2 = at(*add((row, col), directions[1][1]))
        s2 = at(*add((row, col), directions[1][0]))

        mas1 = ''.join((m1, a, s1))
        mas2 = ''.join((m2, a, s2))

        if mas1 in ('MAS', 'SAM') and mas2 in ('MAS', 'SAM'):
            count += 1

print(count)
