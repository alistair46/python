'''The Torris County Visa Center generates the token number for its applicants from their application ID.
The application ID is a numeric value. The token number is generated in a specific form. The even digits in the applicant's ID
are replaced by the digit one greater than the even digit and the odd digits in the applicant's ID are replaced by the digit one
lesser than the odd digit. The numeric value thus generated represents the token number of the applicant.

write an algorith to genrate the token number from the application id

Example
Input
245567

Output
354476

The first digit in the application ID is 2 i.e even. It is replaced by one greater digit ie 3. The second digit is '4' i.e even.
It is replaced by one greater digit Le 5. The third digit is '5' Le odd. It is replaced by one lesser digit Le 4 and so on. 
Hence the output is 354476



'''
t=input()
arr=[int(d) for d in str(t)]
lst=[]
#print(arr)
for i in arr:
    if (i % 2) == 0:
        #print(arr)
        i=i + 1
        lst.append(i)
    else:
        i=i - 1
        lst.append(i)

print(*lst,sep="")
 
