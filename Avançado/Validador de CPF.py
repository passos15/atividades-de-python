 #Validador de cpf.
def validar(cpf): 
    cpf = "".join(filter(str.isdigit, cpf)) #É uma função usada para filtrar apenas os números digitados pelo usuário.

    if len(cpf) != 11 or len (set(cpf)) == 1: #Verifica se realmente o usuário digitou 11 números e se não foram adicionados números iguais(ex: 111.111.111-11).
        return False 
    
    soma = 0 #Primeiro verificador
    for i in range(9): #Fara um loop de 0 a 8.
        soma += int(cpf[i])*(10-i) #Multiplica os nove primeiros números e soma os resultados. 
    resto = soma % 11 #Calcula o resto da divisão da soma por 11.
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    #Se o resto for menor que 2, o dígito é 0; caso contrário, é 11 menos o resto.

    if digito1 != int(cpf[9]):
        return False
    #Verifica se o digitio calculado é igual ao 10° digitado do cpf digitado.

    soma = 0 #Segundo verificador
    for i in range (10): #Fara um loop de 0 a 9.
        soma += int(cpf[i])*(11-i) #Multiplica os 10 primieros números e soma os resultados.
    resto = soma % 11 #Calcula o resto da divisão da soma por 11.
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto  
    #Se o resto for menor que 2, o dígito é 0; caso contrário, é 11 menos o resto.

    if digito2 != int(cpf[10]):
        return False
    #Verifica se o digitio calculado é igual ao 11° digitado do cpf digitado.
    
    return True
    #Se todas as validações passarem, o CPF é válido.

#Pedirá o número do CPF e irá analisar de acordo com o código acima.
cpf_t = input("Digite um CPF para validar: ")
if validar(cpf_t):
    print(f"O CPF {cpf_t} é válido.")
else:
    print(f"O CPF {cpf_t} é inválido.")