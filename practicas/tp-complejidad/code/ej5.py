



def Contiene_Suma(A,n):
    A.sort() # la complejidad es O(nlog(n))
    i=0
    j=len(A)-1
    flag=True
    while flag:
        if i==j:
            return False
        if A[i]+A[j]==n:
            return True
        else:
            if A[i]+A[j]>n:
                j-=1
            else:
                i+=1

A=[1,5,7,9,10,15,23,81,3]
n=8
b=Contiene_Suma(A,n)
print(b)

