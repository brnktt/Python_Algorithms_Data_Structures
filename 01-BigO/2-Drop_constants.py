def print_items(n): #O(n + n = 2n) -> O(n) -> linear(proportional)
    for i in range(n): #O(n) -> linear(proportional)
        print(i)
        
    for j in range(n): #O(n) -> linear(proportional)
        print(j)
        
print_items(10)