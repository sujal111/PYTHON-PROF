#largest items in a collection

import heapq
numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8] 
print(heapq.nlargest(4, numbers))  # [200, 150, 100, 50]
