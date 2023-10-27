def inclui(l, vl, i):
    
    lantes = l[:i]
    ldepois = l[i:]
    lantes.append(vl)
    lnova = lantes+ldepois
    
    return lnova

l = [1,2,4]
inclui(l,3,2)
