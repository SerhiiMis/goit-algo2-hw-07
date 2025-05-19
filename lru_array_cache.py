import random
import time
from functools import lru_cache

# Generate array
N = 100_000
array = [random.randint(1, 100) for _ in range(N)]

# Generate random queries
Q = 50_000
queries = []
for _ in range(Q):
    if random.random() < 0.7:
        l, r = sorted(random.sample(range(N), 2))
        queries.append(("Range", l, r))
    else:
        index = random.randint(0, N - 1)
        value = random.randint(1, 100)
        queries.append(("Update", index, value))

# ------------------ Without Cache ------------------

def range_sum_no_cache(arr, L, R):
    return sum(arr[L:R+1])

def update_no_cache(arr, index, value):
    arr[index] = value

# ------------------ With LRU Cache ------------------

@lru_cache(maxsize=1000)
def cached_range_sum(L, R):
    return sum(array[L:R+1])

def range_sum_with_cache(arr, L, R):
    return cached_range_sum(L, R)

def update_with_cache(arr, index, value):
    arr[index] = value
    cached_range_sum.cache_clear()

# ------------------ Benchmark ------------------

def benchmark(func_range, func_update):
    start = time.time()
    for q in queries:
        if q[0] == "Range":
            func_range(array, q[1], q[2])
        elif q[0] == "Update":
            func_update(array, q[1], q[2])
    return time.time() - start

if __name__ == "__main__":
    print("▶️ Benchmarking without cache...")
    time_no_cache = benchmark(range_sum_no_cache, update_no_cache)
    print(f"Час виконання без кешування: {time_no_cache:.2f} секунд")

    print("\n▶️ Benchmarking with LRU cache...")
    # reset array to ensure same data
    array = [random.randint(1, 100) for _ in range(N)]
    time_with_cache = benchmark(range_sum_with_cache, update_with_cache)
    print(f"Час виконання з LRU-кешем: {time_with_cache:.2f} секунд")
