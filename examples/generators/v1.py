import random

def iter_test():
    remaining_iteration = 100
    while remaining_iteration:
        yield int(random.random() * 100)
        remaining_iteration -= 1

print ",".join([str(i) for i in iter_test()])