from storage import btc_info
btc_str = btc_info()
btc_price = int(btc_str)

class Usuario:
    def __init__(self, id, nome, saldoBRL, saldoBTC, senha):
        self.id = id
        self.nome = nome
        self.saldoBRL = saldoBRL
        self.saldoBTC = saldoBTC
        self.senha = senha

    def to_dict(self):
        return {"id" : self.id, "Nome" : self.nome, "SaldoBTC" : self.saldoBTC, "SaldoBRL" : self.saldoBRL, "senha": self.senha}
    

def sell_btc(user, amount):
    if user["SaldoBTC"] < amount:
        print('Saldo de BTC insuficiente')
        return user
    else:
        user["SaldoBRL"] += amount * btc_price
        user["SaldoBTC"] -= amount
        return user

def buy_btc(user, amount):
    if user["SaldoBRL"] < amount * btc_price:
        print('Saldo insuficiente')
        return user
    else:
        user["SaldoBTC"] += amount
        user["SaldoBRL"] -= btc_price * amount
        return user