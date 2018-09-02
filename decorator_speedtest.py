'''
Original code:
# Time how long it takes for generators vs. lists

import time
gen_start_time = time.time()
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time

print(f"Gen took: {gen_time}")
print(f"List took: {list_time}")

THIS IS A GREAT USE CASE FOR A DECORATOR!
All we really want to do is wrap our function call
with the speedtest code.

'''
from functools import wraps
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Running {fn.__name__}: ")
        print(f"Time elapsed: {end_time - start_time}")
        return result
    return wrapper

@speed_test
def sum_nums_gen():
    return sum(x for x in range(50000000))

@speed_test
def sum_nums_list():
    return sum([x for x in range(50000000)])

print(sum_nums_gen())
print(sum_nums_list())

'''
Running sum_nums_gen: 
Time elapsed: 2.5126240253448486
1249999975000000
Running sum_nums_list: 
Time elapsed: 4.079302072525024
1249999975000000
'''