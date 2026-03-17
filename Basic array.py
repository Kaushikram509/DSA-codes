#finding sum of array elements
#arr = [1,2,3,4,5]
#o/p = 15

def count_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total
arr = [1,2,3,4,5]
print("Sum: ",count_sum(arr))
