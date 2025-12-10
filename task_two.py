def binary_search_upper_bound(sorted_array, target):

    low = 0
    high = len(sorted_array) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        
        if sorted_array[mid] < target:
            low = mid + 1
        else:
            upper_bound = sorted_array[mid]
            high = mid - 1

    return iterations, upper_bound


arr = [0.1, 0.5, 1.3, 2.4, 3.6, 4.8, 5.5, 7.2, 9.9]


print(f"Пошук 3.6: {binary_search_upper_bound(arr, 3.6)}")
# (4, 3.6)

print(f"Пошук 4.0: {binary_search_upper_bound(arr, 4.0)}")
# (3, 4.8)

print(f"Пошук 10.0: {binary_search_upper_bound(arr, 10.0)}")
# (4, None)

print(f"Пошук -2.5: {binary_search_upper_bound(arr, -2.5)}")
# (3, 0.1)