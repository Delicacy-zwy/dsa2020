import sys
data=sys.stdin.read().split()
a=[]
b=[]
num=0
#print (data)
for i in data:
    ##print (i)
    if not (i=='+' or i=='-' or i=='*' or i=='/'):
        if num==0:
            ##print (i)
            b.append(float(i))
            num+=1
        else:
            n1=float(i)
            n2=b.pop()
            k=a.pop()
            if (k=='+'):
                n=n1+n2
            if (k=='*'):
                n=n1*n2
            if (k=='-'):
                n=n2-n1
            if (k=='/'):
                n=n2/n1
            b.append(n)
            num=1
    else:
        a.append(i)
        num=0
while (a):
    n1=b.pop()
    n2=b.pop()    
    k=a.pop()    
    if (k=='+'):
        n=n1+n2
    if (k=='*'):
        n=n1*n2
    if (k=='-'):
        n=n2-n1
    if (k=='/'):
        n=n2/n1
    b.append(n)
print (f'{b[0]:.1f}')