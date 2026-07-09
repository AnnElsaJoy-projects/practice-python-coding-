
import time
l=list(range(10000))
def search(x):
    start=time.perf_counter()
    for i in l:
        if i==x:
           print("Element found")
           break
    end=time.perf_counter()
    print("Time taken:", end-start)
search(9999)       