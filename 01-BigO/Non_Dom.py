def print_items(n): #O((n * n) + n = n^2 + n) -> O(n^2)
    for i in range(n): #O(n) -> linear(proportional)
        for j in range(n): #O(n) -> linear(proportional)
            print(i,j)
    
    for k in range(n): #O(n) -> linear(proportional)
        print(k)

print_items(10)
