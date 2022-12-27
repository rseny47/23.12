p=int(input())
c=1
b=0
while p!=0:
    p=int(input())
    if p!=0:
        c+=1
    if c>b:
        b=c
print(b)