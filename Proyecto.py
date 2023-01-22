import numpy as np
import pandas as pd

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
parsetable.columns=["x","y","z","EOS","S","T"]

#se inicializa el token en 0
token=0
#push del token al stack
stack=np.array([token])
#se lee la cadena y se le agrega EOS al final
cadena=list(input("Ingrese la cadena deseada:"))
cadena=np.append(cadena,"EOS")
#se lee el primer simbolo de la cadena y se borra de la misma
symbol=cadena[0]
cadena=np.delete(cadena,[0])
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
        token=int(x[1])
        symbol=cadena[0]
        cadena=np.delete(cadena,[0])
    
    #si la tabla regresa False imprime que la cadena no se acepta 
    #y se detiene el programa
    elif table=="False":
        print("Cadena no aceptada.")
        quit()

    else:
        #si la tabla regresa reduccion 
        #se hace pop a lo que esta del lado derecho de la regla
        #token toma el valor del top del stack
        #se hace push del lado izquierda de la regla
        #token toma el valor de la tabla 
        #para el token que tenia con el lado izquierdo de la regla
        #se hace push del nuevo token
        if token==4:
            stack=np.delete(stack,[0,1,2,3,4,5])
            token=int(stack[0])
            stack=np.append("S",stack)
            table=tableentry(token,"S")
            x=table.split()
            token=x[1]
            stack=np.append(token,stack)

        elif token==9:
            stack=np.delete(stack,[0,1,2,3,4,5,6,7,8,9])
            token=int(stack[0])
            stack=np.append("S",stack)
            table=tableentry(token,"S")
            x=table.split()
            token=x[1]
            stack=np.append(token,stack)

        elif token==5:
            token=int(stack[0])
            stack=np.append("T",stack)
            table=tableentry(token,"T")
            x=table.split()
            token=x[1]
            stack=np.append(token,stack)

    #se busca el nuevo valor en la tabla y se inicia otra vez el proceso
    table=tableentry(int(token),symbol)

#si al terminar el while lo que queda de la cadena es EOS se acepta la cadena
#si no es asi se rechaza la cadena
if symbol=="EOS":
    print("Cadena Aceptada.")

else:
    print("Cadena no aceptada.")