#conversor de temperatura
def calsius_para_fahrenheit(celsius):
#O def é usado para criar uma função.
    return (celsius *9/5)+32
#o return é usado para calcular e imprimir o resultado.
def fahrenheit_para_celsius(fahrenheit):
    return(fahrenheit-32)*5/9
print("\n===Conversor de temperatura===")
print("1. Celsius para fahrenhet")
print("2. fahrenhet para celsius")
opcao = input("Escolha a conversão (1 ou 2): ")
#Um menu para que o usuário possa escolher a forma de conversão.
if opcao == '1':
    temp_c = float(input("Digite a temperatura em Celsius: "))
    temp_f = calsius_para_fahrenheit(temp_c)
    #Estamos enviando o número digitado pelo usuário para calcular a conversão.
    print(f"{temp_c}°C é igual a {temp_f:.2f}°F.")
elif opcao == '2':
    temp_f = float(input("Digite a temperatura em celsius: "))
    temp_c = fahrenheit_para_celsius(temp_f)
    print(f"{temp_f}°F é igual a {temp_c:.2f}°c.")
else:
    print("opção inválida.")
    #Caso a opção digitada pelo usuário não esteja no menu, imprimir essa mensagem.

