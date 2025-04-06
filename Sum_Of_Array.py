def sumArray(arr):
    #print(type(arr))
    #print(arr)
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sumArray(arr[1:])
    # Please add your code here

# Main
arr=list(map(int, input().strip().split(' ')))
print(sumArray(arr))
#print(sum(arr))