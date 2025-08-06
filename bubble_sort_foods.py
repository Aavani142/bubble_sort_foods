# bubble sort program to sort favorite foods by len

# list of favorite foods
foods = ["Biryani", "Pizza", "Burger", "Dosa", "Shawarma"]

# bubble sort function to sort based on string length
def bubble_sort_by_length(arr):
    n = len(arr)
    # outer loop for all passes
    for i in range(n):
        # inner loop to compare adjacent elements
        for j in range(0, n - i - 1):
            # compare lengths of adjacent elements
            if len(arr[j]) > len(arr[j + 1]):
                # swap if they're in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# print original list
print("Original list:", foods)

# call the sort function
bubble_sort_by_length(foods)

# print sorted list
print("Sorted by length:", foods)
