# DecimalField para numero
# DateTimeField para data
# CharField para texto curto
# TextField para texto comprido

#immportando peewee
import peewee

#craindo o banco de dados
bd = peewee.SqliteDatabase('tabela.db')

class BaseModel(peewee.Model):
    class Meta:
        database = bd

class Author(BaseModel):
    name = peewee.CharField(unique=True)

class Despesas(BaseModel):
    valor = peewee.DecimalField()
    dataPagamento = peewee.DateTimeField()
    dataPagamentoEsperado = peewee.DateTimeField()
    tipoDespesa = peewee.CharField()
    conta = peewee.CharField()

class Receitas(BaseModel):
    valor = peewee.DecimalField()
    dataRecebimento = peewee.DateTimeField()
    dataRecebimentoEsperado = peewee.DateTimeField()
    descrição = peewee.TextField()
    conta = peewee.CharField()
    tipoReceita = peewee.CharField()
    
class Contas(BaseModel):
    saldo = peewee.DecimalField()   
    tipoConta = peewee.CharField()
    instituicaoFinaceira = peewee.CharField()





if __name__ == '__main__':
    try:
        BaseModel.create_table()
        Contas.create_table()
        Despesas.create_table()
        Receitas.create_table()
        print("Tabelas criadas com sucesso!")
    except OperationalError:
        print("Tabela ja existe!")