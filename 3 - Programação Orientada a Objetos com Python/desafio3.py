from abc import ABC, abstractclassmethod, abstractproperty

LIMITE_SAQUES = 3
LIMITE = 500

class Historico:
    def __init__(self):
        self.transacoes = []

    def transacoes(self):
        return self.transacoes
    
    def adicionar_transacao(self, transacao):
        item = {"Tipo": transacao.__class__.__name__, 
                "Valor": transacao.valor}
        self.transacoes.append(item)

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "1000"
        self.cliente = cliente
        self.historico = Historico() 
    
    def saldo(self):
        return (self.saldo)

    def numero(self):
        return (self.numero)

    def agencia(self):
        return (self.agencia)

    def cliente(self):
        return (self.cliente)
    
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
 
    def sacar(self, valor):
        if valor < 0:
            print("Valor inválido!")
        
        elif valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        
        else:
            print("Saldo insuficiente...")
        
        return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Deposito realizado com sucesso!")
            return True
        
        else:
            print("Valor digitado invalido, tente novamente")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=LIMITE, limite_saques=LIMITE_SAQUES):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        print(",")

class Transacao(ABC):

    @abstractclassmethod
    def registrar(self, conta):
        pass

    @property
    @abstractproperty
    def valor(self):
        pass
    
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        validacao = conta.sacar(self.valor)

        if validacao == True:
            conta.historico.adicionar_transacao(self)
        else:
            print("Erro ao realizar Saque...")
    
    @property
    def valor(self):
        return self.valor
    
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        validacao = conta.depositar(self.valor)

        if validacao == True:
            conta.historico.adicionar_transacao(self)
        else:
            print("Erro ao realizar Deposito...")

    def valor(self):
        return self.valor

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

"""
pf = PessoaFisica("joao", "20.03.1990", "000.000.000", "rua imaginaria")
cc = ContaCorrente(2, "pedro")
deposito = Deposito(200)
deposito.registrar(cc)
print(cc.historico.transacoes)"""