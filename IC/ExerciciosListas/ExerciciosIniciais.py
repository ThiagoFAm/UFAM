
# Lista com os k primeiros elementos de uma lista xs
def take(k,xs):
    return xs[0:k]
    
# Lista com os elementos de xs seguintes aos k primeiros
def drop(k,xs):
    return xs[k:]

# Primeiro elemento de uma lista xs
def head(xs):
    return xs[0]
              
# Sublista similar a xs mas sem o primeiro elemento
def tail(xs):
    sublista = xs[1:]
    return sublista

# Ultimo elemento de uma lista xs
def last(xs): 
    return xs[-1]

#Sublista similar a xs mas sem o ultimo elemento
def init(xs):
    sublista = xs[0:-1]
    return sublista

# 2. Numero de matricula = nm // nota = n // frequencia = f
# criterios para aprovação: nota acima de 5 e pelo menos 75 de frequencia

def rfinal(nfs):
    
    aprovados = [(nm) for (nm,n,f) in nfs if n > 5.0 and f >=75]
    reprovados_nota = [(nm) for (nm,n,f) in nfs if n < 5.0]
    reprovados_falta = [(nm) for (nm,n,f) in nfs if f < 75]
    reprovados_nota_falta = [(nm) for (nm,n,f) in nfs if n < 5.0 and f <75]
    
    return aprovados, reprovados_nota, reprovados_falta, reprovados_nota_falta
    

print(head([3,1,4]))

        
 