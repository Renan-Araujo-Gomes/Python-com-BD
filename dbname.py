import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-T2JV7P5;"
    "Database=Pythonnome;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão feita com sucesso")

cursor = conexao.cursor()


id = 3
cliente = "Renanzinho"
produto = "computador"
data = "25/02/2022"
preco = 5000
quantidade = 1

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()
