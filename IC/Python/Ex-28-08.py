def xp(n):
    if n > 0 and n < 100:
        if n % 3 == 0 and n % 5 == 0:return True
        else:return False
    else:return False

def amarelo(x1, y1, x2, y2):
    
    largura = abs(x2 - x1)
    altura = abs(y2 - y1)
    
    areaAmarela = largura * altura
    
    return areaAmarela

    