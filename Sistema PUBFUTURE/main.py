
from re import T
from model import *
from prettytable import PrettyTable



def showReceitas():
    t = PrettyTable(['ID', 'Valor','Data do recebimento','Data do recebimento esperado', 'Descrição', "Tipo de Receita"])

    for receita in Receitas.select():            
        t.add_row([receita.id, receita.valor, receita.dataRecebimento, receita.dataRecebimentoEsperado, receita.descrição, receita.tipoReceita] )
    return t



def showDespesas():
    t = PrettyTable(['ID', 'Valor','Data de pagamento','Data de pagamento esperado', 'Tipo de despesa', "ID da conta"])

    for despesa in Despesas.select():            
        t.add_row([despesa.id, despesa.valor, despesa.dataPagamento, despesa.dataPagamentoEsperado, despesa.tipoDespesa, despesa.conta])
    return t



def showAccounts():
    t = PrettyTable(['ID', 'Tipo de conta','Instituição Finaceira','Saldo'])

    for conta in Contas.select():            
        t.add_row([conta.id, conta.tipoConta, conta.instituicaoFinaceira, conta.saldo])

    return t







print("1- Contas")
print("2- Despesas")
print("3- Receitas")
x = int(input("O que vc gostaria de fazer?"))

#Parte Contas --------------------------------------------------------
if x == 1:
    print("1- criar conta")
    print("2- excluir conta")
    print("3- editar conta")
    print("4- mostrar saldo conta")
    print("5- fazer tranferencia")
    y = int(input("O que vc gostaria de fazer?"))


#Parte criar conta--------------------------------------------------------
    if y == 1:
        saldo = input("saldo: ")
        tipodeconta = input("tipo de conta: ")
        instituiçãofinanceira = input("instituição financeira: ")
        usuario = Contas(saldo = saldo, tipoConta = tipodeconta, instituicaoFinaceira =instituiçãofinanceira)
        usuario.save()  
        print("sua conta foi criada!")


#Parte excluir conta ------------------------------------------------  
    if y == 2:
        print(showAccounts())
        k = input("Selecione por ID qual conta vc deseja excluir: ")
        j = Contas.get(Contas.id == k)
        j.delete_instance()
        j.save()
        print("A conta foi excluida")
        print(showAccounts())


#Parte editar conta -----------------------------------------------------
    if y == 3:
        print(showAccounts())
        k = input("Selecione por ID qual conta vc deseja editar: ")
        print("""
        1 - Saldo
        2 - Tipo de conta
        3 - Instituição financeira""")
        h = int(input("o que vc quer editar na contas? "))
        
        if  h == 1:
            j = Contas.get(Contas.id == k)
            saldoNovo = input("Digite o novo saldo: ")
            j.saldo = saldoNovo
            j.save()
            print(showAccounts())

        if  h == 2:
            j = Contas.get(Contas.id == k)
            tipoContaNovo = input("Digite o novo tipo de conta: ")
            j.tipoConta = tipoContaNovo
            j.save()
            print(showAccounts())

        if  h == 3:
            j = Contas.get(Contas.id == k)
            instituiçãofinanceiraNovo = input("Digite a nova instituição financeira: ")
            j.instituicaoFinaceira = instituiçãofinanceiraNovo
            j.save()
            print(showAccounts())

#Parte mortrar saldo ---------------------------------------------------------------------       
    if y == 4:
        print(showAccounts())
        g = input("Seleceione por id qual conta vc quer ver o saldo:")
        j = Contas.get(Contas.id == g)
        print("O saldo dessa conta é: ", j.saldo)


#Parte fazer tranferencia ---------------------------------------------------------------------
    if y == 5:
        print(showAccounts())
        g = input("Seleceione por id de qual conta vc quer fazer a tranferencia: ")
        j = Contas.get(Contas.id == g)
        print("O saldo dessa conta é: ", j.saldo)
        o = int(input("Quanto vc deseja tirar dessa conta: "))
        j.saldo -= o     
        j.save()
        print(showAccounts())
        u = int(input("Selecione por id para qual conta vvc deseja mandar o dinheiro: "))
        i = Contas.get(Contas.id == u)
        i.saldo += o
        i.save()
        print(showAccounts())


# Parte de despesas ------------------------------------------------------------
if x == 2:
    print("1- cadastrar despesa")
    print("2- Editar despesa")
    print("3- Remover despesa")
    print("4- Listar despesas")
    print("5- Filtrar por periodo")
    print("6- Filtrar por tipo de despesa")
    y = int(input("O que vc gostaria de fazer?"))


#Parte cadastrar despesa ----------------------------------------------------
    if y == 1:   
        valor = input("valor: ")
        dataPagamento = input("Data do pagamento [yyyy-mm-dd]: ")
        dataPagamentoEsperado = input("Data do pagamento esperado [yyyy-mm-dd]: ")
        tipoDespesa = input("Tipo de despesa: ")
        print(showAccounts())
        conta = input("Selecione por id para qual conta é a despeza: ")
        j = Contas.get(Contas.id == conta)
        usuario = Despesas(valor = valor, dataPagamento = dataPagamento, dataPagamentoEsperado = dataPagamentoEsperado, tipoDespesa = tipoDespesa, conta = conta)
        usuario.save()  
        print("sua despesa foi criada!")
        print(showDespesas())


#Parte editar despesa---------------------------------------------------------
    if y == 2:
        print(showDespesas())
        k = input("Selecione por ID qual despesa vc deseja editar: ")
        print("""
        1 - valor
        2 - Data de pagamento
        3 - Data de pagamento esperado
        4 - Tipo de despesa
        """)
        h = int(input("o que vc quer editar na contas? "))
        
        if  h == 1:
            j = Despesas.get(Despesas.id == k)
            valorNovo = input("Digite o novo valor: ")
            j.valor = valorNovo
            j.save()
            print(showDespesas())

        if  h == 2:
            j = Despesas.get(Despesas.id == k)
            dataPagamentoNovo = input("Digite a nova data de pagamento:  ")
            j.dataPagamento = dataPagamentoNovo
            j.save()
            print(showDespesas())

        if  h == 3:
            j = Despesas.get(Despesas.id == k)
            dataPagamentoEsperadoNovo = input("Digite a nova data de pagamento esperado:  ")
            j.dataPagamentoEsperado = dataPagamentoEsperadoNovo
            j.save()
            print(showDespesas())   

        if  h == 4:
            j = Despesas.get(Despesas.id == k)
            tipoDespesaNovo = input("Digite a novo tipo de despesa:  ")
            j.tipoDespesa = tipoDespesaNovo
            j.save()
            print(showDespesas())

#Parte excluir despesa -------------------------------------------------------------
    if y == 3:
        print(showDespesas())
        k = input("Selecione por ID qual despesa vc deseja excluir: ")
        j = Despesas.get(Despesas.id == k)
        j.delete_instance()
        j.save()
        print("A conta foi excluida")
        print(showDespesas())


#Parte listar receitas ------------------------------------------------------------------           
    if y == 4:
        print(showDespesas())


#Parte filtrar por data -----------------------------------------------------------------------
    if y == 5:
        p = int(input("""Como vc deseja filtrar?
            1 - Maior que determinada data
            2 - Menor que determinada data
            3 - Entre duas datas
            """))

        if p == 1:
            filtro = str(input("A partir de qual data vc deseja ver as despesas[yyyy-mm-dd]: "))
            t = PrettyTable(['ID', 'Valor','Data de pagamento','Data de pagamento esperado', 'Tipo de despesa', "ID da conta"])
            for i in Despesas.select().where(Despesas.dataPagamento > filtro):       
                t.add_row([i.id, i.valor, i.dataPagamento, i.dataPagamentoEsperado, i.tipoDespesa, i.conta])
            print(t)
        
        if p == 2:
            filtro = str(input("A partir de qual data vc deseja ver as despesas[yyyy-mm-dd]: "))
            t = PrettyTable(['ID', 'Valor','Data de pagamento','Data de pagamento esperado', 'Tipo de despesa', "ID da conta"])
            for i in Despesas.select().where(Despesas.dataPagamento < filtro):       
                t.add_row([i.id, i.valor, i.dataPagamento, i.dataPagamentoEsperado, i.tipoDespesa, i.conta])
            print(t)

        if p == 3:
            print("Quais são as dois intrevalos de data que vc deseje filtrar? Use essa formatação[yyyy-mm-dd]")
            filtrode = input("DE: ")
            filtroate = input("ATÉ: ")
            t = PrettyTable(['ID', 'Valor','Data de pagamento','Data de pagamento esperado', 'Tipo de despesa', "ID da conta"])
            for i in Despesas.select().where(Despesas.dataPagamento.between(filtrode, filtroate)):
                
                 t.add_row([i.id, i.valor, i.dataPagamento, i.dataPagamentoEsperado, i.tipoDespesa, i.conta])
            print(t)


#Parte filtro por tipo de despesa ---------------------------------------------------------------
    if y == 6:
        filtro = str(input("Qual tipo de conta vc gostaria de filtrar: "))
        t = PrettyTable(['ID', 'Valor','Data de pagamento','Data de pagamento esperado', 'Tipo de despesa', "ID da conta"])
        for i in Despesas.select().where(Despesas.tipoDespesa == filtro):       
            t.add_row([i.id, i.valor, i.dataPagamento, i.dataPagamentoEsperado, i.tipoDespesa, i.conta])
        print(t)



if x == 3:
    print("1- cadastrar despesa")
    print("2- Editar despesa")
    print("3- Remover despesa")
    print("4- Listar despesas")
    print("5- Filtrar por periodo")
    print("6- Filtrar por tipo de despesa")
    y = int(input("O que vc gostaria de fazer?"))


#Parte cadastrar receita ----------------------------------------------------
    if y == 1:   
        valor = input("valor: ")
        dataRecebimento = input("Data do recebimento [yyyy-mm-dd]: ")
        dataRecebimentoEsperado = input("Data do recebimento esperado [yyyy-mm-dd]: ")
        descrição = input("Descrição: ")
        tipoReceita = input("Tipo de receita: ")
        print(showAccounts())
        conta = input("Selecione por id para qual conta é a receita: ")
        j = Contas.get(Contas.id == conta)
        usuario = Receitas(valor = valor, dataRecebimento = dataRecebimento, dataRecebimentoEsperado = dataRecebimentoEsperado, descrição = descrição, conta=j, tipoReceita = tipoReceita)
        usuario.save()  
        print("sua receita foi criada!")
        print(showReceitas())


#Parte editar receitas---------------------------------------------------------
    if y == 2:
        print(showReceitas())
        k = input("Selecione por ID qual despesa vc deseja editar: ")
        print("""
        1 - valor
        2 - Data de pagamento
        3 - Data de pagamento esperado
        4 - Descrição
        5 - Tipo de Receita
        """)
        h = int(input("o que vc quer editar na contas? "))
        
        if  h == 1:
            j = Receitas.get(Receitas.id == k)
            valorNovo = input("Digite o novo valor: ")
            j.valor = valorNovo
            j.save()
            print(showReceitas())

        if  h == 2:
            j = Receitas.get(Receitas.id == k)
            dataRecebimentoNovo = input("Digite a nova data de recebimento [yyyy-mm-dd]:  ")
            j.dataRecebimento = dataRecebimentoNovo
            j.save()
            print(showReceitas())

        if  h == 3:
            j = Receitas.get(Receitas.id == k)
            dataRecebimentoEsperadoNovo = input("Digite a nova data de recebimento esperado [yyyy-mm-dd]:  ")
            j.dataRecebimentoEsperado = dataRecebimentoEsperadoNovo
            j.save()
            print(showReceitas())   

        if  h == 4:
            j = Receitas.get(Receitas.id == k)
            descriçãoNovo = input("Digite a descriçaõ:  ")
            j.descriçaõ = descriçãoNovo
            j.save()
            print(showReceitas())

        if  h == 5:
            j = Receitas.get(Receitas.id == k)
            tipoReceitaNovo = input("Digite o novo tipo:  ")
            j.tipoReceita = tipoReceitaNovo
            j.save()
            print(showReceitas())

#Parte excluir receita -------------------------------------------------------------
    if y == 3:
        print(showReceitas())
        k = input("Selecione por ID qual receita vc deseja excluir: ")
        j = Receitas.get(Receitas.id == k)
        j.delete_instance()
        j.save()
        print("A conta foi excluida")
        print(showReceitas())


#Parte listar receitas ------------------------------------------------------------------           
    if y == 4:
        print(showReceitas())


#Parte filtrar por data -----------------------------------------------------------------------
    if y == 5:
        p = int(input("""Como vc deseja filtrar?
            1 - Maior que determinada data
            2 - Menor que determinada data
            3 - Entre duas datas
            """))

        if p == 1:
            filtro = str(input("A partir de qual data vc deseja ver as receitas[yyyy-mm-dd]: "))
            t = PrettyTable(['ID', 'Valor','Data de recebimento','Data de recebimento esperado', "Descrição", "ID da conta"])
            for i in Receitas.select().where(Receitas.dataRecebimento > filtro):       
                t.add_row([i.id, i.valor, i.dataRecebimento, i.dataRecebimentoEsperado, i.descrição, i.conta])
                
            print(t)
        
        if p == 2:
            filtro = str(input("A partir de qual data vc deseja ver as receitas[yyyy-mm-dd]: "))
            t = PrettyTable(['ID', 'Valor','Data de recebimento','Data de recebimento esperado', "Descrição" ,"ID da conta"])
            for i in Receitas.select().where(Receitas.dataRecebimento < filtro):       
                t.add_row([i.id, i.valor, i.dataRecebimento, i.dataRecebimentoEsperado, i.descrição, i.conta ])
            print(t)

        if p == 3:
            print("Quais são as dois intrevalos de data que vc deseje filtrar? Use essa formatação[yyyy-mm-dd]")
            filtrode = input("DE: ")
            filtroate = input("ATÉ: ")
            t = PrettyTable(['ID', 'Valor','Data de pagamento','Data de pagamento esperado', 'Tipo de despesa', "ID da conta"])
            for i in Receitas.select().where(Receitas.dataRecebimento.between(filtrode, filtroate)):
                
                 t.add_row([i.id, i.valor, i.dataRecebimento, i.dataRecebimentoEsperado, i.descrição, i.conta ])
            print(t)


#Parte filtro por tipo de receita ---------------------------------------------------------------
    if y == 6:
        filtro = str(input("Qual tipo de receita vc gostaria de filtrar: "))


        t = PrettyTable(['ID', 'Valor','Data de recebimento','Data de recebimento esperado', 'Descrição', "ID da conta"])
        for i in Receitas.select().where(Receitas.tipoReceita == filtro):       
            t.add_row([i.id, i.valor, i.dataRecebimento, i.dataRecebimentoEsperado, i.descrição, i.conta ])
        print(t) 
