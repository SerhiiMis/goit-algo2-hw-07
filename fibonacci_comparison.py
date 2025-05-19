import timeit
import matplotlib.pyplot as plt
from functools import lru_cache

# ------------------ LRU Cache Fibonacci ------------------

@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

# ------------------ Splay Tree Fibonacci ------------------

class SplayNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def _splay(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            if root.left is None:
                return root
            if key < root.left.key:
                root.left.left = self._splay(root.left.left, key)
                root = self._rotate_right(root)
            elif key > root.left.key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right:
                    root.left = self._rotate_left(root.left)
            return self._rotate_right(root) if root.left else root
        else:
            if root.right is None:
                return root
            if key > root.right.key:
                root.right.right = self._splay(root.right.right, key)
                root = self._rotate_left(root)
            elif key < root.right.key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left:
                    root.right = self._rotate_right(root.right)
            return self._rotate_left(root) if root.right else root

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def insert(self, key, value):
        if not self.root:
            self.root = SplayNode(key, value)
            return
        self.root = self._splay(self.root, key)
        if key == self.root.key:
            self.root.value = value
            return
        node = SplayNode(key, value)
        if key < self.root.key:
            node.right = self.root
            node.left = self.root.left
            self.root.left = None
        else:
            node.left = self.root
            node.right = self.root.right
            self.root.right = None
        self.root = node

    def get(self, key):
        self.root = self._splay(self.root, key)
        if self.root and self.root.key == key:
            return self.root.value
        return None

def fibonacci_splay(n, tree):
    cached = tree.get(n)
    if cached is not None:
        return cached
    if n < 2:
        tree.insert(n, n)
        return n
    result = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, result)
    return result

# ------------------ Benchmark & Plot ------------------

def benchmark():
    values = list(range(0, 951, 50))
    lru_times = []
    splay_times = []

    for n in values:
        # LRU
        lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=10) / 10
        lru_times.append(lru_time)

        # Splay
        tree = SplayTree()
        splay_time = timeit.timeit(lambda: fibonacci_splay(n, tree), number=10) / 10
        splay_times.append(splay_time)

    # Table
    print(f"{'n':<10}{'LRU Cache Time (s)':<20}{'Splay Tree Time (s)':<20}")
    print("-" * 50)
    for n, lru, splay in zip(values, lru_times, splay_times):
        print(f"{n:<10}{lru:<20.8f}{splay:<20.8f}")

    # Plot
    plt.plot(values, lru_times, marker='o', label='LRU Cache')
    plt.plot(values, splay_times, marker='x', label='Splay Tree')
    plt.title("Порівняння часу виконання для LRU Cache та Splay Tree")
    plt.xlabel("Число Фібоначчі (n)")
    plt.ylabel("Середній час виконання (секунди)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    benchmark()
