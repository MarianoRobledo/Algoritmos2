A=[7,10,8,6,5,4,3,1,9,2]

mitad=int(len(A)/2)
cantidad=int(mitad/2)
contador=0
extra=0


for i in range(0,mitad-1):
    if A[i]<mitad:
        contador +=1
print(contador)
if contador==cantidad:
    print(A)
else:
    if contador > cantidad:
        extra=contador-cantidad
        for i in range(1,extra):
            for j in range(0,mitad-1):
                if A[j]<mitad:
                    for k in range(mitad,len(A)-1):
                        if A[k]>mitad:
                            value=A[k]
                            A[k]=A[j]
                            A[j]=value
                            break
                    break
    else:
        extra=cantidad-contador
        for i in range(0,extra):
            for j in range(0,mitad-1):
                if A[j]>mitad:
                    for k in range(mitad,len(A)-1):
                        if A[k]<mitad:
                            value=A[k]
                            A[k]=A[j]
                            A[j]=value
                            break
                    break
                

print(A)


