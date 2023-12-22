import pytz 
import datetime 
class Account:
    #depois refatorar para criar uma conta

    @staticmethod
    def _dataHoraAtual():
        fusoBR = pytz.timezone('Brazil/East')
        dataHoraAtual = datetime.now(fusoBR)
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
        return self._saldo #print(f"Saldo Atual da conta é de R${self._saldo}")
    
    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append(f"""valor depositado: {valor}\nSaldo Atual: {self._saldo}\nData transação: {self._dataHoraAtual}""")

    def sacar(self, valor):
        if self._excedeLimite(valor):
            return
        self._saldo -= valor
        return 
    
    def _excedeLimite(self, valor):
        if (self._saldo - valor) < self._limiteConta():
            print('Você não tem saldo suficiente na conta para sacar esse valor')
            self.consultaSaldo()
            return True
        return False

    def _limiteConta(self):
        self._limite = -200
        return self._limite

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, Account._dataHoraAtual()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((-valor, self._saldo, Account._dataHoraAtual()))

    def consultarHistoricoTransacoes(self):
        print("Histórico de Transações")
        for transacao in self._transacoes:
            print(transacao)






