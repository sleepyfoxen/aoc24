
with open('input', 'r') as f:
    rules, updates = map(str.splitlines, f.read().strip().split('\n\n'))

pairs = [ tuple(rule.split('|')) for rule in rules ]
# pairs are like (47, 53) meaning 47 must appear before 53

def check(pages, pairs=pairs):
    for i, page in enumerate(pages):
        for lhs, rhs in pairs:
            if page in rhs and lhs in pages:
                if pages.index(lhs) > i:
                    return False

    return True

corrects, incorrects = [], []
for update in updates:
    pages = update.split(',')
    if check(pages): corrects.append(pages)
    else: incorrects.append(pages)

total = sum(int(c[len(c)//2]) for c in corrects)
print(total)


orders = []
for pages in incorrects:
    order = []
    while len(pages):
        for page in pages:
            for lhs, rhs in pairs:
                if page in lhs and rhs in pages:
                    break  # can't insert this page yet
            else:
                order.insert(0, page)

        pages.remove(order[0])
    orders.append(order)

total = sum(int(o[len(o)//2]) for o in orders)
print(total)
