
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
        if not (abs(next_level - level) <= 3 and next_level != level):
            return False
    
    return True


# part 1
safe_count = len(tuple(filter(safe, reports)))
print(safe_count)

# part 2
for report in filter(lambda r: not safe(r), reports):
    for i in range(len(report)):
        if safe(report[:i] + report[i+1:]):
            safe_count += 1
            break

print(safe_count)
