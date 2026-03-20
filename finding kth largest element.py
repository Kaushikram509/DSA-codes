#iKth largest element in array
def selection_sort(arr, k):
    n = len(arr)

    for i in range (n):
        max_index = i

        for j in range(i+1, n):
            if(arr[j] > arr[max_index]):
               max_index = j
        
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr[k-1]

arr = [64, 25, 12, 22, 11]
k = int(input("Enter the number: "))
print(k,"number from beginning: ",selection_sort(arr, k))
