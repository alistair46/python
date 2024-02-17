'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
 After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

fname = input("Enter File Name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
for line in fh :
    if line.startswith('From ') :
        words = line.split()
        req = words[1]
        counts[req] = counts.get(req,0) + 1
        bigword = None
        bigcount = None
for word, count in counts.items() :
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count
print(bigword,bigcount)