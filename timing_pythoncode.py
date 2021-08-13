# focus on theree ways 1. simply tracking time elapsed
# 2 using timeit module
# 3 special %%timeit module only for jupyter notebook
from timeit import timeit


def func_one(n):
    return [str(num) for num in range(n)]


print(func_one(10))


def func_two(n):
    return list(map(str, range(n)))

print(func_two(10))

import time
# ( time eclapse = current time before we run code - current time after running code)

start_time = time.time()
result = func_one(100000)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)  #0.01795029640197754

start_time = time.time()
result = func_two(100000)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time) #0.015958547592163086 so func_two is faster
# above method is not efficient for the samll value and is hard to find which one is better

# better method below for jupyter notebook
# %%timeit
# func_one(100) #easy in jupyter note book
# %%timeit
# func_two(100)





