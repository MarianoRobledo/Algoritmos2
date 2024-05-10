class dictionaryNode:
    value=None
    key=None
    nextNode=None

class dictionary:
    head=None

def funcionHash(key,m):
    return key % m

def insert(D, key,  value):
    k=funcionHash(key,len(D))
    if D[k] is None:
        L=[]
        t=key,value
        L.append(t)
        D[k]=L
    else:
        L=D[k]
        t=(key,value)
        L.append(t)

def search(D, key):
    k=funcionHash(key,len(D))
    if D[k] is None:
        return None
    else:
        L=D[k]
        for keys in L:
            if keys[0] == key:
                return keys[1]

def delete(D,key):
    k=funcionHash(key,len(D))
    if D[k] is None:
        return D
    else:
        L=D[k]
        for keys in L:
            if keys[0] == key:
                t=keys[0],keys[1]
                L.remove(t)
                return D


