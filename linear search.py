def linear_search(arr, target):
    count = 0
    for num in arr:
        if(num == target):
            count += 1
    return count
arr = [50,20,40,10,60,30,30,29,30,10,20,40,30,40,30,20,66,39]
target = 30
print("count: ", linear_search(arr, target))
