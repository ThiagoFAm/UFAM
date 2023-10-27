def pag(a,b,c):
    if  a + b == c :  return True
    elif a + c == b: return True
    elif b + a == c: return True
    elif c + a == b: return True
    elif b + c == a: return True
    elif c + b == a: return True
    else:
        return True

def pgp(vl,i):
    
    if i < 2: return 0.10 * vl
    if i > 2 and i < 10: return 0.5 * vl
    if i >= 60: return 0.6 * vl
    else: return vl
    
def rentcar(km, d):
    diariaCar = 60
    kmRodado = 0.15
    return (d * diariaCar + km * 0.15)  
    