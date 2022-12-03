import numpy as np
import pandas as pd

tablaparse=np.array([
    [False, False, "shift 1", False, "shift 13", False, False],
    ["shift 2", False, "shift 6", False, False, "shift 3", False],
    ["shift 2", False, "shift 6", False, False, "shift 7", False],
    [False, "shift 4", "shift 8", False, False, False, "shift 5"],
    [False, "shif 4", "shift 8", False, False, False, "shift 9"],
    [False, False, "shift 10", False, False, False, False],
    ["m_z", "m_z", "m_z", False, False, False, False],
    ["shift 11", False, False, False, False, False, False],
    [False, "n_z", "N_z", False, False, False, False],
    [False, "shift 12", False, False, False, False, False],
    [False, False, False, "s_zmnz", False, False, False],
    ["m_ama", "m_ama", "m_ama", False, False, False, False],
    [False, "n_nbn", "n_nbn", False, False, False, False],
    [False, False, False, True, False, False, False]
])

def tableentry (token,symbol):
    return parsetable.loc[token,symbol]

parsetable=pd.DataFrame(tablaparse)
parsetable.columns=["a","b","z","EOS","S","M","N"]

token=0
cont=0
stack=np.array([token])
cadena=list(input("Ingrese la cadena deseada:"))
cadena=np.append(cadena,"EOS")
print("Cadena:")
print(cadena)
print("Stack:")
print(stack)
symbol=cadena[0]
cadena=np.delete(cadena,[0])
print("Cadena:")
print(cadena)
table=tableentry(token,symbol) 
while table != "True":
    x=table.split()
    if x[0]=="shift":
        stack=np.append(symbol,stack)
        stack=np.append(x[1],stack)
        #print("Stack:")
        #print(stack)
        token=int(x[1])
        symbol=cadena[0]
        cadena=np.delete(cadena,[0])
        #print("Cadena:")
        #print(cadena)

    elif table=="False":
        print("Cadena no aceptada.")
        break

    else:
        if token==6:
            stack=np.delete(stack,[0,1])
            token=int(stack[0])
            stack=np.append("M",stack)
            table=tableentry(token,"M")
            x=table.split()
            token=x[1]            
            stack=np.append(token,stack)
            #print("Stack:")
            #print(stack)

        elif token==11:
            stack=np.delete(stack,[0,1,2,3,4,5])
            token=int(stack[0])
            stack=np.append("M",stack)
            table=tableentry(token,"M")
            x=table.split()
            token=x[1]
            stack=np.append(token,stack)
            #print("Stack:")
            #print(stack)

        elif token==8:
            stack=np.delete(stack,[0,1])
            token=int(stack[0])
            stack=np.append("N",stack)
            table=tableentry(token,"N")
            x=table.split()
            token=x[1]            
            stack=np.append(token,stack)
            #print("Stack:")
            #print(stack)

        elif token==12:
            stack=np.delete(stack,[0,1,2,3,4,5])
            token=int(stack[0])
            stack=np.append("N",stack)
            table=tableentry(token,"N")
            x=table.split()
            token=x[1]
            stack=np.append(token,stack)
            #print("Stack:")
            #print(stack)

        elif token==10:
            stack=np.delete(stack,[0,1,2,3,4,5,6,7])
            token=int(stack[0])
            stack=np.append("S",stack)
            table=tableentry(token,"S")
            x=table.split()
            token=x[1]
            stack=np.append(token,stack)
            #print("Stack:")
            #print(stack)

        else:
            print(token)
            print('hi')
            break
    
    table=tableentry(int(token),symbol)
    print("Stack:")
    print(stack)
    print("Cadena:")
    print(cadena)

if symbol=="EOS":
    print("Cadena Aceptada.")

else:
    print("Cadena no aceptada.")