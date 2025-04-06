# cook your dish here

a = int(input())

for i in range(a):
    n = int(input())
    arr = []
    for k in range(n):
        arr.append(int(input()))
        
    count = 0
    for j in arr:
        if j%2 != 0:
            count = count + 1
    print(count)    
