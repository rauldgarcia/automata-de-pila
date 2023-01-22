import numpy as np
import pandas as pd

'''tablaparse=np.array([
    [False, False, "shift 1", False, "shift 13", False, False],
    ["shift 2", False, "shift 6", False, False, "shift 3", False],
    ["shift 2", False, "shift 6", False, False, "shift 7", False],
    [False, "shift 4", "shift 8", False, False, False, "shift 5"],
    [False, "shift 4", "shift 8", False, False, False, "shift 9"],
    [False, False, "shift 10", False, False, False, False],
    ["m_z", "m_z", "m_z", False, False, False, False],
    ["shift 11", False, False, False, False, False, False],
    [False, "n_z", "N_z", False, False, False, False],
    [False, "shift 12", False, False, False, False, False],
    [False, False, False, "s_zmnz", False, False, False],
    ["m_ama", "m_ama", "m_ama", False, False, False, False],
    [False, "n_nbn", "n_nbn", False, False, False, False],
    [False, False, False, True, False, False, False]
])'''

tablaparse=np.array([
    ["shift 2", False, False, False, "shift 1", False],
    [False, False, False, True, False, False],
    ["shift 2", "shift 5", False, False, "shift 3", False],
    [False, False, "shift 4", False, False, False],
    [False, False, "S_xSz", "S_xSz", False, False],
    [False, "T_lambda", False, False, False, "shift 7"],
    [False, "T_labmda", False, False, False, False],
    [False, "shift 8", False, False, False, False],
    [False, False, "shift 9", False, False, False],
    [False, False, "S_xyTyz", "S_xyTyz", False, False]    
])

def tableentry (token,symbol):
    return parsetable.loc[token,symbol]

parsetable=pd.DataFrame(tablaparse)
#parsetable.columns=["a","b","z","EOS","S","M","N"]
parsetable.columns=["x","y","z","EOS","S","T"]

#se inicializa el token en 0
token=0
#push del token al stack
stack=np.array([token])
#se lee la cadena y se le agrega EOS al final
cadena=list(input("Ingrese la cadena deseada:"))
cadena=np.append(cadena,"EOS")
print("Cadena:")
print(cadena)
print("Stack:")
print(stack)
print()
#se lee el primer simbolo de la cadena y se borra de la misma
symbol=cadena[0]
print("symbol:")
print(symbol)
cadena=np.delete(cadena,[0])
print("Cadena:")
print(cadena)
#se llama al valor de tabla parse
table=tableentry(token,symbol) 
#mientras la tabla no de un true se ejecutara
while table != "True":
    x=table.split()
    #si la tabla regresa un shift se hace push al simbolo
    #el token ahora es el indicado en el shift y se hace push de el
    #y se lee el siguiente simbolo de la cadena
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

    #si la tabla regresa False imprime que la cadena no se acepta y se detiene el programa
    elif table=="False":
        print("Cadena no aceptada.")
        quit()

    else:
        '''if token==6:
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
            #print(stack)'''
        
        #si la tabla regresa reduccion se hace pop a lo que esta del lado derecho de la regla
        #token toma el valor del top del stack
        #se hace push del lado izquierda de la regla
        #token toma el valor de la tabla para el token que tenia con el lado izquierdo de la regla
        #se hace push del nuevo token
        if token==4:
            stack=np.delete(stack,[0,1,2,3,4,5])
            token=int(stack[0])
            stack=np.append("S",stack)
            table=tableentry(token,"S")
            x=table.split()
            token=x[1]
            stack=np.append(token,stack)
            #print("Stack:")
            #print(stack) 

        elif token==9:
            stack=np.delete(stack,[0,1,2,3,4,5,6,7,8,9])
            token=int(stack[0])
            stack=np.append("S",stack)
            table=tableentry(token,"S")
            x=table.split()
            token=x[1]
            stack=np.append(token,stack)
            #print("Stack:")
            #print(stack)

        elif token==5:
            token=int(stack[0])
            stack=np.append("T",stack)
            table=tableentry(token,"T")
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
    print("symbol:")
    print(symbol)
    print()

#si al terminar el while lo que queda de la cadena es EOS se acepta la cadena
#si no es asi se rechaza la cadena
if symbol=="EOS":
    print("Cadena Aceptada.")

else:
    print("Cadena no aceptada.")