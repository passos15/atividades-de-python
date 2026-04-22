n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
n3 = float(input('digite a terceira nota: '))
media = (n1 + n2 + n3) / 3 
if media >= 7:
    print('aprovado')   
else:   
     print('reprovado') 
print(f'sua média é: {media:.1f}')
#O :.1f diz: "Exiba apenas 1 casa após o ponto floating (decimal)" // em alguns casos pode se usar :.2f para exibir 2 casas decimais.