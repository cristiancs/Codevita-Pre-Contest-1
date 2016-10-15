from collections import deque

cantidad = int(input(""))


def getentero(char):
    return ord(char)-96

for i in range(0, cantidad):
    # Para cada caso de prueba
    costo = 0
    string = input()
    diff = {}   #positiva implica puedo borrar/reemplazar, negativa debo agregar
    for letter in string:
        if(letter not in diff):
            diff[letter] = -getentero(letter)+1
        else:
            diff[letter]+=1
    cola = deque()
    for k,v in diff.items():
        reemplazado = False
        while(v < 0):
            # Reemplazar mientras podamos
            if(not reemplazado):
                for k1,v1 in diff.items():
                   while(v1 > 0 and v < 0):
                        costo+=1
                        v1-=1
                        v+=1
                   if v == 0:
                        diff[k1] = v1
                        break
                   diff[k1]=v1
                reemplazado = True
            else:
                #llego la hora de agregar
                costo+=2
                v+=1
        diff[k] = v
        if v > 0:
            cola.append(k)

    # Revisamos la cola
    for elem in list(cola):
        #Solo podemos borrar elementos
        v = diff[elem]
        while(v > 0):
            costo+=3
            v-=1
        diff[k] = 0
    print(str(costo) + "\n")



