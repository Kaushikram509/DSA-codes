def bubble_sort(arr):
    n = len(arr)
    c=0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if(arr[j]%2==0 and arr[j+1] %2==0):
                if(arr[j] > arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
                    c+=1
            if(not swapped):
                break
    return arr, c

arr = [8,5,4,2,6,1,3]
print(bubble_sort(arr))
