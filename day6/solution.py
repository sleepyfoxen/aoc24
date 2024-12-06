from collections import defaultdict

with open('input', 'r') as f:
    data = f.read().strip().splitlines()

indicators = '^>v<'
rows, cols = len(data), len(data[0])

# guard starting location
for row, line in enumerate(data):
    for col, character in enumerate(line):
        if character in indicators:
            guard = (row, col)
            direction = indicators.index(character)
            start = (guard, direction)
            break


path = set()
while True:
    path.add(guard)
    match direction:
        case 0: next_row, next_col = (guard[0] - 1, guard[1])
        case 1: next_row, next_col = (guard[0], guard[1] + 1)
        case 2: next_row, next_col = (guard[0] + 1, guard[1])
        case 3: next_row, next_col = (guard[0], guard[1] - 1)

    if next_row not in range(rows) or next_col not in range(cols):
        break

    match data[next_row][next_col]:
        case '#':
            direction += 1
            direction %= 4
        case _:
            guard = next_row, next_col

print(len(path))


count = 0
for (row, col) in path:
    guard, direction = start
    visited = defaultdict(set)

    while True:
        if guard in visited[direction]:
            count += 1
            break

        visited[direction].add(guard)
        match direction:
            case 0: next_row, next_col = (guard[0] - 1, guard[1])
            case 1: next_row, next_col = (guard[0], guard[1] + 1)
            case 2: next_row, next_col = (guard[0] + 1, guard[1])
            case 3: next_row, next_col = (guard[0], guard[1] - 1)

        if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
            break

        next_tile = data[next_row][next_col]
        if (next_row, next_col) == (row, col) and not (row, col) == start[0]:
             next_tile = '#'

        match next_tile:
            case '#':
                direction += 1
                direction %= 4
            case _:
                guard = next_row, next_col

print(count)
