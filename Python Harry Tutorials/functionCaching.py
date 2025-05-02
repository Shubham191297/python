import functools
import time

# using cache, function will be memoized

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print(fx(2))
print(fx(7))

# now for this value it will simply return from cache hence will not run it again.
print(fx(2))