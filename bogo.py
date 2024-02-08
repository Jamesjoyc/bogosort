import random

def bogo_sort(a):
    attempts = 0
    while not is_sorted(a):
        shuffle(a)
        attempts += 1
        print(attempts)
        if attempts > 100000000000000000000000000000000:  # Limit the number of attempts to avoid potential infinite loop
            raise Exception("Bogo Sort took too many attempts, possibly due to inefficient implementation.")
    return a

def is_sorted(a):
    return all(a[i] <= a[i+1] for i in range(len(a)-1))

def shuffle(a):
    n = len(a)
    for i in range(n):
        r = random.randint(0, n-1)
        a[i], a[r] = a[r], a[i]

# Example usage:
unsorted_list = [3, 1, 4, 1,8,4,66,565,667,34,5454,5,4,54545]
sorted_list = bogo_sort(unsorted_list)
print("Sorted List:", sorted_list)
