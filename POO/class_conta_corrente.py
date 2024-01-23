from class_conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self):
        self.__limite = 0.0

    def abrirConta(self, nb = 0, na = 0, nc = "", titular = "", saldo = "", limite = 0.0):
        self._nbanco = nb
        self._nagencia = na
        self._nconta = nc
        self._titular = titular
        self._saldo = saldo
        self.__limite = limite
        print("A conta "+self._nconta+" do Sr(a). "+self._titular+" foi aberta")

    def sacar(self, valor):
        
        if(valor > self._saldo+self.__limite):
            print("Saldo Insuficiente!")
        
        elif(valor <= self._saldo):
            self._saldo -= valor
            print("Você realizou um saque de "+str(valor)+" o seu saldo atual é "+str(self._saldo))

        else:
            sobra = valor - self._saldo
            self.__limite -= sobra
            self._saldo = 0
            print("O valor sacado é "+str(valor)+" \no saldo atual é: "+str(self._saldo)+" \no seu limite atual é: "+str(self.__limite))
