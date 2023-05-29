def print_items(n): #O(n * n = n^2) -> O(n^2) -> squared
    for i in range(n): #O(n) -> linear(proportional)
        for j in range(n): #O(n) -> linear(proportional)
            print(i, j)
        
print_items(10)