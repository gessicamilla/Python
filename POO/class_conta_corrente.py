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