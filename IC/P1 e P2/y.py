def permuta(ks,xs):
    l1 = []
    l2 = []
    for n in ks:
        if n in xs:
            count = xs.count(n)
            l1.append((n,count))
        else:
            return False
    for n in xs:
        if n in ks:
            count = ks.count(n)
            l2.append((n,count))
        else:
            return False
    print(f"{l1}\n{l2}")
    for (x,y) in l1:
        if (x,y) in l2:
            return True
        
def test(nome):
    nome = list(nome)  # Convert the input to a list of characters
    result = []  # List to store the count of each letter

    for n in nome:
        if n.isalpha():
            count = nome.count(n)
            found = False
            for i in result:
                if result[i] == n:
                    found = True
                    break

            if not found:
                result.append((n, count))

    return result

        
    return result

print(test("thiagothiago"))