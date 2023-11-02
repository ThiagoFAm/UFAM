#1
def pedrap(x,y):
    if (x >= 0 and x < 7) and (y >= 0 and y < 7):
        return True
    else:
        return False

#2
def maop(mao):

    if len(mao) != 7:
        return False

    for par in mao:
        valor1, valor2 = par
        if valor1 not in range(0, 7) or valor2 not in range(0, 7):
            return False

    return True

#3
def carrocap(x,y):
    if pedrap(x,y) and x==y:
        return True
    else: return False
    
#4 
def tem_carroca_p(mao): 
    for (x,y) in mao:
        if carrocap(x,y) == True: return True
        else: return False
        
#5
def tem_carrocas(mao): 
    return [(x,y) for (x,y) in mao if carrocap(x,y) == True]
    