def test(xs):
    falta = [(a,x,i) for (a,x,i) in xs if i < 75]
    nota = [(a,x,i) for (a,x,i) in xs if x < 5]
    nf = [(a,x,i) for (a,x,i) in xs if i < 75 and x < 5]
    nf2 = [(a,x,i) for (a,x,i) in xs if i >= 75 and x >= 5]
    return (f"{falta}\n{nota}\n{nf}\n{nf2}")

print(test([("nofa", 4, 75),("eef", 5, 74),("rfc", 5, 75), ("cao", 4, 74)]))