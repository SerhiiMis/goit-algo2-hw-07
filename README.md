# 🧠 Cache Optimization Algorithms — LRU Cache & Splay Tree

## 📌 Homework: goit-algo2-hw-10

This project contains two tasks focused on optimizing data access and computation using different caching techniques:

1. **Task 1** — Use **LRU cache** to optimize range queries in a large array
2. **Task 2** — Compare performance of **Fibonacci calculation** using `@lru_cache` and a **Splay Tree**

---

## 🔧 Task 1: Range Sum Optimization with LRU Cache

### 🛠 Requirements

- Functions:
  - `range_sum_no_cache(array, L, R)` — simple summation
  - `update_no_cache(array, index, value)` — updates value at index
  - `range_sum_with_cache(array, L, R)` — summation with `@lru_cache(maxsize=1000)`
  - `update_with_cache(array, index, value)` — updates array and invalidates relevant cached results
- Generate:
  - Array of size `N = 100_000` with random integers
  - List of `Q = 50_000` random queries: `[("Range", L, R), ("Update", index, value), ...]`
- Compare execution time:
  - With and without LRU cache
- Use: `time.time()` or `time.perf_counter()` to measure duration

### ✅ Output Example

```
Час виконання без кешування: 3.11 секунд
Час виконання з LRU-кешем: 0.02 секунд
```

---

## 🔧 Task 2: Fibonacci — LRU Cache vs Splay Tree

### 🛠 Requirements

- Functions:
  - `fibonacci_lru(n)` — recursive with `@lru_cache`
  - `fibonacci_splay(n, tree)` — manually stores/loads values from a Splay Tree
- Measure performance for values of `n`:
  ```python
  values = [0, 50, 100, ..., 950]
  ```
- Measure execution time using `timeit`
- Plot a graph with `matplotlib`
  - X-axis: `n`
  - Y-axis: average execution time
  - Two lines: `LRU Cache`, `Splay Tree`

### ✅ Output Example (Console)

```
n         LRU Cache Time (s)  Splay Tree Time (s)
--------------------------------------------------
0         0.00000028          0.00000020
50        0.00000217          0.00000572
...
```

### 📊 Output Example (Graph)

- Title: `Порівняння часу виконання для LRU Cache та Splay Tree`
- Axis labels: `Число Фібоначчі (n)` and `Середній час виконання (секунди)`
- Legend: LRU Cache (🔵), Splay Tree (🟠)

---

## ✅ How to Run

```bash
python lru_array_cache.py
python fibonacci_comparison.py
```

---
