def redo(numero):
    decimal=numero%1
    if decimal<0.5:
        numero=int(numero)
    else:
        numero=int(numero+1)
    return numero

# numero=0
# numero=float(input("ingrese un rno "))

# print(redo(numero))
