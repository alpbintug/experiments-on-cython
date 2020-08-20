import time
while True:
    i=0
    cur = time.time()
    print(type(cur))
    next = time.time()
    while next -cur < 0.001:
        i+=1
        next = time.time()
    print(i)