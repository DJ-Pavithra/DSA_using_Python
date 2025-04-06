arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(len(arr)-arr[::-1].index(x)-1)