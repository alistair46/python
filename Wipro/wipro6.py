'''
Design a way to sort a list of positive integers in descending order 
based on the frequency of elements.

Input: 
Consists of two arguments

Size: no of elements
Arr: list of positive integers

Output: 
Return a list of +ve integers sorted according to frequency of elements

input-
size 19
arr = {1,2,2,3,3,3,4,4,5,5,5,5,6,6,6,7,8,9,10}
output-
{5,5,5,5,3,3,3,6,6,6,2,2,4,4,1,7,8,9,10}
'''
'''n=int(input())
arr=list(map(int,input().strip().split()))
arr.sort()
#print(arr)

flag = 0

for i in range(len(arr)):
    maxE=max(maxE,arr[i])
    if i in arr:
        i==i
        flag=flag+1
        count=flag
print(count)

freq=[0]*(maxE+1)

for i in range(maxE+1):
    if (freq[i]>1):
        value = 100000 - i
        arr[count] = 100000 * freq[i] + value
        count= count+1
return count
'''
def sortbyfreq(arr,n):
    maxE = -1
    for i in range(n):
        maxE=max(maxE,arr[i])

    freq=[0]*(maxE+1)

    count = 0
    for i in range(n):
        freq[arr[i]] +=1

    for i in range(maxE+1):
        if (freq[i]>0):
            value=100000 -i
            arr[count]=100000 * freq[i] + value
            count +=1
    return count

def printsortedarray(arr,count):
    for i in range(count):
        frequency= arr[i]/100000
        value = 100000 -(arr[i]%100000)

        for j in range(int(frequency)):
            print(value,end=" ")

if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().strip().split()))
    count=sortbyfreq(arr,n)
    arr.sort(reverse = True)

    printsortedarray(arr,count)
    
