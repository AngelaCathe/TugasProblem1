def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] != 0:  # Memeriksa apakah elemen bukan nol
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def move_zeros_to_end(arr):
    quicksort(arr, 0, len(arr) - 1)

# Contoh penggunaan
array = [1, 2, 0, 1, 0, 7, 0, 5, 0]
move_zeros_to_end(array)
print(array)