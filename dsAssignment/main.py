import threading

from dsAssignment import assignment

for i in range(1, 11):
    t = threading.Thread(target=assignment.pool_coverage, args=(i,))
    t.start()
    print(i)
