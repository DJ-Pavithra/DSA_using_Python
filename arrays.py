#each index corresponds to each month
arr=[2200,2350,2600,2130,2190]
# 1.  In Feb, how many dollars you spent extra compare to January?
print(arr[1]-arr[0])
#2. Find out your total expense in first quarter (first three months) of the year.
print(sum(arr[:3]))
#3. Find out if you spent exactly 2000 dollars in any month
diff = 2000
for i in range(len(arr)-1):
    if arr[i]==diff:
        print("Yes")
        break
    else:
        print("No")
        break
#or
if 2000 in arr:
    print("Yes")
else:
    print('No')
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
arr.append(1980)
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
arr[3]=arr[3]-200
print(arr)

