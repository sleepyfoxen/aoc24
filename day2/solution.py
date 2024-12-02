
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

    if report not in (sorted(report), sorted(report, reverse=True)):
        return False
    
    for level, next_level in zip(report, report[1:]):
        if not 0 < abs(next_level - level) <= 3:
            return False
    
    return True


unsafe_reports, safe_reports = [], []
for report in reports:
    (unsafe_reports, safe_reports)[safe(report)].append(report)

# part 1
print(len(safe_reports))

# part 2
for report in unsafe_reports:
    for i in range(len(report)):
        if safe(report[:i] + report[i+1:]):  # try with each character removed
            safe_reports.append(report)
            break

print(len(safe_reports))
