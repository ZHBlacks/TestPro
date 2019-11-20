'''
Created on 2019年11月14日

@author: Veryci
'''
def bubbleSort(arr):
    n = len(arr)
    
    # 遍历所有数组
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
arr = [64,35,25,63,73,83,37,65,2,7]

bubbleSort(arr)

print(arr)

print("排序后的数组：")
for i in range(len(arr)):
    print("%d" %arr[i])