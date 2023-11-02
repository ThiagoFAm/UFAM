from Parte1 import *

#6
def pedras(listaPedras): 
    return [x + y for (x,y) in listaPedras]
    

#7 
def garagem(listaPedrasResto):
    x = pedras(listaPedrasResto)
    return (sum(x[0:])//5)*5

#8
def pedra_igual_p(pedra1,pedra2): 
    if pedra1[0] == pedra2[1] and pedra1[1] == pedra2[0]:
        return True
    if pedra1[0] == pedra2[0] and pedra1[1] == pedra2[1]:
        return True
    else: return False

#9
def ocorre_pedra_p(pedra, mao):
    for (x,y) in mao:
        if pedra_igual_p(pedra, (x,y)) == True:
            return True
    else: return False
 
#10
def ocorre_valor_p(ponta, mao):
    for pedra in mao:
        if ponta in pedra:
            return True
    return False

#11  
def ocorre_pedra(pontadapedra, mao):
    return [pedra for pedra in mao if pontadapedra in pedra]
    
#12
def pedra_maior(mao):
    maior_pedra = mao[0]
    maior_soma = maior_pedra[0] + maior_pedra[1]

    for pedra in mao:
        soma_pontas = pedra[0] + pedra[1]
        if soma_pontas > maior_soma:
            maior_pedra = pedra
            maior_soma = soma_pontas

    return maior_pedra

#13
def ocorre_valor_q(pedra, mao):
    valor_pedra = pedras(pedra)
    return [(x,y) for (x,y) in mao if pedras([(x,y)]) == valor_pedra ]

#14
def ocorre_carroca_q(mao):
    carrocas = [(x,y) for (x,y) in mao if x == y]
    return len(carrocas)


def semrep(xs):
    lista = []
    return [x for x in xs if x not in lista]
    
    
   
        
    

print(semrep([1,2,2,2,3,4]))