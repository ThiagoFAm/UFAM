def placas(string):
    placa = list(string)
    resultado = []
    if len(placa) != 7: return "nada"
    else:
        for i in placa:
            print(i)
            if i.isalpha():
                resultado.append("L")
            elif i.isdigit():
                resultado.append("N")
        resultado2 = "".join(resultado)
        if  resultado2 == "LLLNNLN":
            return "moto"
        elif resultado2 == "LLLNLNN":
            return "carro"
        else: return "nada"
            

