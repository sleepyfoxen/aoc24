
with open('input', 'r') as f:
    data = f.read().strip().splitlines()

indicators = '^>v<'
guard = ()
direction = None

grid = (len(data), len(data[0]))
print(grid)

# guard starting location
for row, line in enumerate(data):
    for col, character in enumerate(line):
        if character in indicators:
            guard = (row, col)
            direction = indicators.index(character)

start = (guard, direction)

visited = set()
while True:

    visited.add(guard)

    match direction:
        case 0: next_tile = (guard[0] - 1, guard[1])
        case 1: next_tile = (guard[0], guard[1] + 1)
        case 2: next_tile = (guard[0] + 1, guard[1])
        case 3: next_tile = (guard[0], guard[1] - 1)
    
    try:
        print(direction, next_tile, data[next_tile[0]][next_tile[1]])
    except IndexError:
        break

    match data[next_tile[0]][next_tile[1]]:
        case '#':
            direction += 1
            direction %= 4
        case _:
            guard = next_tile

print(len(visited))
print()
print()

# raise

obstacles = set()
for (row, col) in visited:
    guard, direction = start
    visited_ = set()

    while True:
        if (guard, direction) in visited_:
            obstacles.add((row, col))
            break

        visited_.add((guard, direction))

        match direction:
            case 0: next_tile = (guard[0] - 1, guard[1])
            case 1: next_tile = (guard[0], guard[1] + 1)
            case 2: next_tile = (guard[0] + 1, guard[1])
            case 3: next_tile = (guard[0], guard[1] - 1)
        
        if next_tile[0] < 0 or next_tile[1] < 0:
            break

        try:
            next_tile_data = data[next_tile[0]][next_tile[1]]
        except IndexError:
            break

        if next_tile == (row, col):
            if not (row, col) == start[0]:
                next_tile_data = '#'

        match next_tile_data:
            case '#':
                direction += 1
                direction %= 4
            case _:
                guard = next_tile

print(obstacles, len(obstacles))  # 2292 is too high
