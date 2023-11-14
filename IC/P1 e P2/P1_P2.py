#p1.1
def tret(l1, l2, l3):
    # Verifique se a soma dos quadrados dos dois lados menores é igual ao quadrado do lado maior.
    # Se isso for verdade, o triângulo é retângulo.
    lados = [l1, l2, l3]
    lados.sort()
    
    if lados[0]**2 + lados[1]**2 == lados[2]**2:
        return True
    else:
        return False
    
#p1.2

def pontos(a, b, c, d):
    # Calcula todas as quatro possíveis somas
    sums = [a + c, a + d, b + c, b + d]
    
    # Verifica se alguma das somas é múltiplo de 5
    for soma in sums:
        if soma % 5 == 0:
            return soma
    
    # Se nenhuma das somas for múltipla de 5, retorna 0
    return 0

#p1.3

def posv(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    # Verifica se o movimento é válido para um cavalo (em L)
    if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
        return True
    else:
        return False

#p1.4

def pgp(vl, i):
    if i >= 60:
        # Passageiros com 60 anos ou mais pagam 50% do preço padrão
        return 0.5 * vl
    elif i <= 10:
        # Crianças até 10 anos pagam 40% do preço padrão
        return 0.4 * vl
    elif i < 2:
        # Bebês (menos de 2 anos) pagam apenas 10%
        return 0.1 * vl
    else:
        # Passageiros com idade normal pagam o preço padrão
        return vl

#p2.1

def totalfreq(ks, xs):
    result = []
    for k in ks:
        count = xs.count(k)
        result.append((k, count))
    return result

#p2.2

def eventos(ag, d):
    result = []
    for e, i, f in ag:
        if i <= d <= f:
            result.append(e)
    return result

#p2.3

def tmv(pt, mao):
    matching_stones = [stone for stone in mao if pt in stone]
    if matching_stones:
        max_stone = max(matching_stones, key=lambda x: max(x))
        mao.remove(max_stone)
        return mao
    else:
        return mao

#p2.4

def retira(ks, xs): 
    return [x for x in xs if x not in ks]
    

def norep(xs): 
    result = []
    for i in xs:
        if i in result:
            pass
        else:
            result.append(i)
    return result

print(norep([1,2,3,3,3,3,3,4,4,5,1,2]))
