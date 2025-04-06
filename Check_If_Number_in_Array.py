def checkNumber(arr, x):
    i = 0

    for i in range(len(arr)):
        if arr[i] == x:
            return True    
    return False


# Main


print("Enter the elements of the array:")
arr = list(map(int, input().strip().split()))  # Read array elements
print("Enter the number to search:")
x = int(input())  # Read number to search

if checkNumber(arr, x):
    print('true')
else:
    print('false')
