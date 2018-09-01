





# g = (yield num for num in range(1, 10))  WRONG! DON'T NEED TO ADD YIELD
# g = (num for num in range(1,10))
# print(g)  # <generator object <genexpr> at 0x104005780>  GENERATOR EXPRESSION
# print(next(g))
#
# def nums():
#     for num in range(1,10):
#         yield num
#
# f = nums()
# print(f)  # <generator object nums at 0x1015d6bf8>  GENERATOR FUNCTION
# print(next(f))
#
# print(sum(num for num in range(1,10)))


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