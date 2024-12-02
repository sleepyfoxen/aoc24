
with open('input', 'r') as f:
    data = f.read().strip().splitlines()

reports = []

for line in data:
    levels = [ int(level) for level in line.split(' ') ]
    reports.append(levels)


def safe(report):
    # two conditions:
    # - consecutive elements differ by at most 3
    # - sequence is strictly monotonic

    for level, next_level in zip(report, report[1:]):
        if not 0 < abs(next_level - level) <= 3:
            return False

    return report in (sorted(report), sorted(report, reverse=True))


unsafe_reports, safe_reports = [], []
for report in reports:
    (unsafe_reports, safe_reports)[safe(report)].append(report)

# part 1 - how many reports meet the safety condition?
print(len(safe_reports))

# part 2 - how many meet the safety condition with one element removed?
for report in unsafe_reports:
    if any(safe(report[:i] + report[i+1:]) for i in range(len(report))):
        safe_reports.append(report)

print(len(safe_reports))
