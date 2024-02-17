'''
Our Client eBay wants to run a campaign on their website, which will have the following parameters - eBay wants that on certain x 
products, they want to calculate the final pricing, for each product on eBay there will be a tock unit parameter, this parameter 
will denote how many items are there in the fulfilment centre. Now, a positive number would denote that the units of items in the 
fulfilment centre and thus can be shipped to the customer.Also, the price for each product varies based on the distance of the 
user from the fulfilment centre and the customers doors. But more that each product may be in different fulfilment centre.
Now, these values are 00'KMS for each centurion KMs. The prices will increase by the factor distance, you have tofind the max 
discounted price for each product that can be shipped. Following are the input/output parameters

Input:

First Line contains the number of products
The second line has the prices for each of these products
The third line has shipping distance for each of these products
The fourth line will have the SKU's

Output -
It will contain the final price of each of the possible product SKU's

Sample Input:
6
87 103 229 41 8 86
3 1 9 2 1 2
7 -21 30 0 -4 -3

Sample Output:
261 2061
'''
it=int(input())
price=list(map(int,input().strip().split()))
distance=list(map(int,input().strip().split()))
sku_lst=list(map(int,input().strip().split()))
finallst = []

for i in range(0, len(sku_lst)):
    if sku_lst[i] > 0:
        finallst.append(price[i]*distance[i])

print(" ".join(str(it) for it in finallst))






