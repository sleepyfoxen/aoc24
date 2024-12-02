
with open('input', 'r') as f:
    data = f.read().strip().splitlines()

reports = []

for line in data:
    levels = [ int(level) for level in line.split(' ') ]
    reports.append(levels)


def safe(report):
    # two conditions:
    # - sequence is strictly monotonic
    # - consecutive elements differ by at most 3

    ordered_report = sorted(report)

    if not (report == ordered_report or report == ordered_report[::-1]):
        return False
    
    for level, next_level in zip(report, report[1:]):
        if abs(next_level - level) <= 3 and next_level != level:
            continue
        else:
            return False
    
    return True


# part 1
count = 0
for _ in filter(safe, reports):
    count += 1

print(count)

# part 2
count = 0
for report in reports:
    if safe(report):
        count += 1
        continue

    any_safe = False
    for i in range(len(report)):  # remove all single levels
        if safe(report[:i] + report[i+1:]):
            any_safe = True
            break
    
    if any_safe:
        count += 1

print(count)
