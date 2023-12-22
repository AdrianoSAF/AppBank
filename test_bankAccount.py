from BankAccount import Account


def test_depositarConsultarSaldo():
    minhaConta = Account("adriano", "333.333.333-33",1222,1233)
    minhaConta.depositar(500)
    assert minhaConta.consultaSaldo() == 500

def test_SacarComSaldoSemSaldo():
    minhaConta = Account("adriano", "333.333.333-33",1222,1233)
    minhaConta.depositar(1000)
    minhaConta.sacar(500)
    assert minhaConta.consultaSaldo() == 500

    minhaConta.sacar(1000)
    assert minhaConta.consultaSaldo() == 500





    