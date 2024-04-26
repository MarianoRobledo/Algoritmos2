class Trie:
    root=None

class TrieNode:
    parent=None
    children=None
    key=None
    IsEndOfWord=False


def crearLista():
    lista=[None]*26
    return lista

def insert(T,element):
    if T.root == None:
        T.root=crearLista()
    element=element.lower()
    current=T.root
    total=len(element)-1
    for i,v in enumerate(element):
        if current[ord(v)-97] is None:
            newNode=TrieNode()
            newNode.key=v            
            newNode.children=crearLista()
            if total==i:
                newNode.IsEndOfWord=True
                current[ord(v)-97]=newNode
            elif i==0:
                currentRet=newNode
                current[ord(v)-97]=newNode
                current=current[ord(v)-97].children  
            else:
                newNode.parent=currentRet
                currentRet=newNode
                current[ord(v)-97]=newNode
                current=current[ord(v)-97].children            
        else:
            currentRet=current[ord(v)-97]
            current=current[ord(v)-97].children
            
def search(T,element):
    current=T.root
    total=len(element)-1
    element=element.lower()
    for i,v in enumerate(element):
        if current[ord(v)-97] is not None:
            if i==total :
                if current[ord(v)-97].IsEndOfWord==True :
                    return True
                else:
                    return False
            else:
                current=current[ord(v)-97].children
        else:
            return False
    

def prueba(T,element):
    current=T.root
    for i,v in enumerate(element):
        print(current[ord(v)-97].children.count(None))
        current=current[ord(v)-97].children
            
def delete(T,element):
    current=T.root
    total=len(element)-1
    contador=0
    element=element.lower()
    inicio=TrieNode()
    bifurcacion=TrieNode()
    siguiente=""
    if search(T,element):
        for i,v in enumerate(element):
            if i==0:
                inicio=current[ord(v)-97]
                bifurcacion=inicio
            if current[ord(v)-97].children.count(None)<25:
                bifurcacion=current[ord(v)-97]
                siguiente=element[i+1]
            if i==total and current[ord(v)-97].children.count(None)<26:
                current[ord(v)-97].IsEndOfWord=False
                return True
            current=current[ord(v)-97].children
        if inicio==bifurcacion:
            T.root[ord(inicio.key)-97]=None
            return True
        else:
            bifurcacion.children[ord(siguiente)-97]=None
            return True
    else:
        return False
    
    
    
        
        


