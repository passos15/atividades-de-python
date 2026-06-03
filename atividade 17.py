#Sistema Bancário
class ContaBancaria: #Class é o conjunto de características e comportamentos que caracterizam todos os objetos que pertencem a essa classe.
    def __init__(self, numero_conta, titular, saldo_inicial = 0): #O método __init__ é o construtor da classe, que é invocado automaticamente quando um objeto é criado.
        self.numero_conta = numero_conta #O self é um indicador que se refere ao próprio objeto que está sendo criado ou manipulado em uma classe.
        self.saldo = saldo_inicial
        self.titular = titular

    #Método de deposito.
    def depositar (self, valor):
        if valor > 0: #Se o valor for maior que 0 o usuário consegue depositar.
            self.saldo += valor #Atualiza o saldo. equivalente a self.saldo = self.saldo + valor.
            print(f"Deposito de R$ {valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Valor de depósito inválido.")
    
    #Método de sacar.
    def sacar (self, valor):
        if valor > 0 and self.saldo >= valor: #Verifica se o valor do saque é positivo e se o saldo é suficiente, se verdadeiro, realiza o saque.
            self.saldo -= valor #Vai subtrair o valor da conta com o valor do saque.
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
            return True #Indica que o saque foi realizado com sucesso.
        elif valor > self.saldo:
            print("Valor de saque inválido.")
            return False #Indica que o saque não foi realizado.
        else:
            print("valor de saque inválido.")
            return False

    def verificar (self):
        print(f"Saldo atual da conta {self.numero_conta}: R${self.saldo:.2f}")
        return self.saldo #Retorna o valor do saldo.

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = [] #Cria uma lista vazia para guardar as contas.

    #Método de adicionar conta.
    def adicionar_conta(self, conta):
        self.contas.append(conta) #Adiciona a conta à lista.
        print(f"Conta {conta.numero_conta} adicionada ao cliente {self.nome}")


    #Método de listar contas.
    def listar_contas(self):
        if self.contas:
            print(f"\nContas de {self.nome}: ")
            for conta in self.contas: #Percorre cada elemento na lista.
                print(f"Número: {conta.numero_conta}, saldo: R${conta.saldo:.2f}")
            else:
                print(f"O cliente {self.nome} não possui conta.")

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = [] #Cria uma lista vazia para guardar os clientes do banco.

    #Método de adicionar cliente.
    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente) #Adiciona o objeto cliente à lista.
        print(f"Cliente {cliente.nome} adicionado ao banco {self.nome}.")

    #Método de buscar cliente por cpf.
    def buscar_por_cpf(self, cpf):
        for cliente in self.clientes: #Percorre cada cliente na lista self.clientes.
            if cliente.cpf == cpf: #Verifica se o CPF do cliente atual é igual ao CPF buscado.
                return cliente #Retorna o cliente encontrado.
        return None #Se nenhum cliente for encontrado, retorna None.
    
    #Método debuscar cliente por número.
    def buscar_por_numero(self, numero_conta):
        for cliente in self.clientes: # Percorre cada cliente do banco.
            for conta in cliente.contas: # Percorre cada conta do cliente
                if conta.numero_conta == numero_conta: #Verifica se o número do cliente atual é igual ao número buscado.
                    return conta
        return None
    
#Exemplo de uso do sistema bancário
banco_digital = Banco("Meu Banco Digital")

cliente1 = Cliente("Cassia Passos", "321.654.987-00")
conta1_Cassia = ContaBancaria("001-X", "Cassia Passos", 1000)
conta2_Cassia = ContaBancaria("002-Y", "Cassia Passos", 500)
cliente1.adicionar_conta(conta1_Cassia)
cliente1.adicionar_conta(conta2_Cassia)
banco_digital.adicionar_cliente(cliente1)

cliente2 = Cliente("Ionei Souza", "987.654.321-00")
conta1_Ionei = ContaBancaria("003-Z", "Ionei Souza", 2000)
cliente2.adicionar_conta(conta1_Ionei)
banco_digital.adicionar_cliente(cliente2)

# Operações
cliente1.listar_contas()
conta1_Cassia.depositar(300)
conta1_Cassia.sacar(800)
conta1_Cassia.verificar()

cliente_encontrado = banco_digital.buscar_por_cpf("321.654.987-00")
if cliente_encontrado:
    print(f"\nCliente encontrado: {cliente_encontrado.nome}")

conta_encontrada = banco_digital.buscar_por_numero("003-Z")
if conta_encontrada:
    print(f"Conta encontrada: {conta_encontrada.numero_conta} do titular {conta_encontrada.titular}")