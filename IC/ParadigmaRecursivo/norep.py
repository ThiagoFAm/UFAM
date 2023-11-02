def norep(xs):
    if len(xs) == 0 : return []
    else:
        x = xs[0]
        rest = norep([i for i in xs[1:] if i != x])
        return [x] + rest
        
    
xs = [1,1,2,3,4]

print(norep(xs))