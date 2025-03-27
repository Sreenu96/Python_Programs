#Print count the devisors of given number

num = int(input("Enter a number:"))
d=1
while d<=num:
    if num%d==0:
        print(d)
    d=d+1