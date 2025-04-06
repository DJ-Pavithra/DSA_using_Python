def power(a,b):
    result = 1
    for i in range(b):
        result = a * result
    return result

a,b = map(int,input().split())
print(power(a,b))