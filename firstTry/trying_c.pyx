import time
cpdef int i
cpdef float th
th = 0.001
while True:
    i=0
    cur = time.time()
    next = time.time()
    while (next - cur < th):
        i+=1
        next = time.time()
    print(i)