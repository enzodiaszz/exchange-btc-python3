from storage import btc_info, salvar, verificador_senha, verificador_id, busca_usuario
from models import Usuario, buy_btc, sell_btc


btc_str = btc_info()
btc_preco = int(btc_str)
while True:
    log = int(input('  1 - Entrar \n 2 - Cadastrar \n Escolha:  '))
    if log == 1:
        identifier = int(input('Digite seu ID: '))
        id_searcher = verificador_id(identifier)
        if id_searcher:
            senha_real = verificador_senha(identifier)
            passtry = str(input('Digite sua senha:   '))
            if passtry == senha_real:
                print('Login bem sucedido!')
                user = busca_usuario(id_searcher)
                

            else:
                print('Senha incorreta, execute de novo.')
                break
        else:
            print('ID não encontrado')
            break
    

    elif log == 2:
        escolha_id = int(input('Escolha seu ID: '))
        if escolha_id < 0:
            print('Id inválido')
            break
        id_searcher = verificador_id(escolha_id)
        if escolha_id == id_searcher:
            print('Esse ID já existe, execute de novo')
            break
        escolha_nome = str(input('Digite seu primeiro nome: '))
        deposito_btc = float(input('Deposite seus BTC: '))
        deposito_real = float(input('Deposite um valor em Reais: '))
        cadastro_senha = str(input('Cadastre uma senha:  '))
        cadastrado = Usuario(escolha_id, escolha_nome, deposito_real, deposito_btc, cadastro_senha)
        saving = cadastrado.to_dict()  
        salvar(saving)
        continue
    else:
        print('Opção Inválida')
        break

    
    while True:
        escolha = int(input(f'\n \n \n \n \n \n \n--- BTC EXCHANGE --- \n Olá {user["Nome"]}! \n Preço Atual: {btc_preco}R$ \n Saldo em R$: {user["SaldoBRL"]:.2f} \n Saldo em BTC: {user["SaldoBTC"]} \n 1 - Comprar BTC \n 2 - Vender BTC \n 3 - Sair \n Escolha:  '))
        if escolha == 1:
            qtd = float(input('Quantidade de BTC a ser comprada:  '))
            buy_btc(user, qtd)

        elif escolha == 2:
            qtd = float(input('Quantidade de BTC a ser vendida:  '))
            sell_btc(user, qtd)
    
        elif escolha == 3:
            final_user = Usuario(user["id"], user["Nome"], user["SaldoBTC"], user["SaldoBRL"], user["senha"])
            final_save = final_user.to_dict()
            salvar(final_save)
            print('Fechando programa...')
            break