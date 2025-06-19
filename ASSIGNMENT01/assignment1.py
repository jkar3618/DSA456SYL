import random
import time

def bubble_sort(my_list):
    n = len(my_list)
    ops = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            ops += 1  # Comparison operation
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                ops += 1  # Swap operation
    return my_list, ops

def selection_sort(my_list):
    n = len(my_list)
    ops = 0

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            ops += 1  # Comparison operation
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        if i != min_idx:
            my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
            ops += 1  # Swap operation
    return my_list, ops

def insertion_sort(my_list):
    n = len(my_list)
    ops = 0

    for i in range(1, n):
        key = my_list[i]
        j = i - 1
        ops += 1  # Store key
        while j >= 0 and key < my_list[j]:
            ops += 1  # Comparison
            my_list[j + 1] = my_list[j]
            j -= 1
            ops += 1  # Shift
        my_list[j + 1] = key
        ops += 1  # Insert key
    return my_list, ops

def quick_sort(mylist):
    ops = [0]  # Use list to allow modification inside nested function

    def _quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = []
        middle = []
        right = []

        for x in arr:
            ops[0] += 1  # Comparison
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                middle.append(x)
        return _quick_sort(left) + middle + _quick_sort(right)

    sorted_list = _quick_sort(mylist)
    return sorted_list, ops[0]

def insertion_sort_range(mylist, left, right):
    ops = 0
    for i in range(left + 1, right + 1):
        key = mylist[i]
        j = i - 1
        ops += 1  # Store key
        while j >= left and mylist[j] > key:
            ops += 1  # Comparison
            mylist[j + 1] = mylist[j]
            j -= 1
            ops += 1  # Shift
        mylist[j + 1] = key
        ops += 1  # Insert key
    return mylist, ops


def main():
    import copy

    # Test datasets for best, worst, and average cases
    best_case = list(range(100))              # Already sorted (best case)
    worst_case = list(range(99, -1, -1))      # Reverse order (worst case)
    avg_case = random.sample(range(100), 100) # Random order (average case)

    # List of sorting algorithms to test
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Quick Sort", quick_sort),
    ]

    # Run each algorithm on best, worst, and average cases
    for name, func in algorithms:
        print(f"\n{name}:")
        for case_name, data in [("Best", best_case), ("Worst", worst_case), ("Average", avg_case)]:
            data_copy = copy.deepcopy(data)  # Make a copy to avoid in-place modification
            _, ops = func(data_copy)         # Sort and count operations
            print(f"{case_name} Case T(n): {ops}")

    # Test insertion_sort_range (partial sorting of index 10 to 30)
    print("\nInsertion Sort (Range):")
    sample = random.sample(range(100), 100)
    _, ops = insertion_sort_range(sample, 10, 30)
    print(f"Partial sort (10~30) T(n): {ops}")


def measure_time(sort_func, data):
    start = time.time()
    sort_func(data.copy())  # Copy to avoid in-place sorting affecting next runs
    end = time.time()
    return end - start

def run_step4():
    sizes = [10, 50, 100, 500, 1000, 5000]
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Quick Sort", quick_sort),
    ]

    print("\nStep 4: Sort Execution Time vs Input Size (Worst Case)")
    print(f"{'Algorithm':<20} {'n=10':>10} {'n=50':>10} {'n=100':>10} {'n=500':>10} {'n=1000':>10} {'n=5000':>10}")

    for name, func in algorithms:
        times = []
        for n in sizes:
            worst_case = list(range(n, 0, -1))  # Worst case: descending
            duration = measure_time(func, worst_case)
            times.append(f"{duration:.5f}")
        print(f"{name:<20} {''.join(f'{t:>10}' for t in times)}")

# Entry point
if __name__ == "__main__":
    main()
    run_step4()
