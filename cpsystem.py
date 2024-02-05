import random

def cp():
    def calcular_digito_verificador(parcial):
        soma = 0
        peso = len(parcial) + 1

        for d in parcial:
            soma += int(d) * peso
            peso -= 1

        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    nove_digitos = [str(random.randint(0, 9)) for _ in range(9)]
    digito1 = calcular_digito_verificador(nove_digitos)
    
    dez_digitos = nove_digitos + [str(digito1)]
    digito2 = calcular_digito_verificador(dez_digitos)

    cpf_gerado = ''.join(dez_digitos + [str(digito2)])
    return f"{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}"

# Exemplo de uso
def exibircpf():

    cpf_gerado = cp()
    print("CPF Gerado:", cpf_gerado)
