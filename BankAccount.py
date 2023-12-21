from pytz import timezone
from datetime import now, strftime
class Account:
    #depois refatorar para criar uma conta

    @staticmethod
    def _dataHoraAtual():
        fusoBR = timezone('Brazil/East')
        dataHoraAtual = now(fusoBR)
        return dataHoraAtual.strftime("%d/%m/%Y %H:%M:%S")

    def __init__(self, name, cpf, agencia, numeroConta):
        self._name = name
        self.__cpf = cpf
        self._saldo = 0 #método para alterar o saldo
        self._limite = None #método para ver o limite/Aumentar limite
        self.__agencia = agencia #Não pode alterar.
        self.__numeroConta = numeroConta
        self._transacoes = []
        self.cartoes = []

    def consultaSaldo(self):
        return print(f"Saldo Atual da conta é de R${self._saldo}")
    
    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append(f"""valor depositado: {valor}\nSaldo Atual: {self._saldo}\nData transação: {self._dataHoraAtual}""")




