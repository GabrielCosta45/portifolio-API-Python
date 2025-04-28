from src.extracao.extrair_dados import extrair_dados
from src.tratamento.tratar_dados import tratar_produtos, tratar_usuarios, tratar_carrinhos

# Extrair dados
df_produtos, df_usuarios, df_carrinhos = extrair_dados()

# Tratar os dados
df_produtos = tratar_produtos(df_produtos)
df_usuarios = tratar_usuarios(df_usuarios)
df_carrinhos = tratar_carrinhos(df_carrinhos)

# Exibir os resultados
print("Produtos tratados:")
print(df_produtos.head())

print("Usuários tratados:")
print(df_usuarios.head())

print("Carrinhos tratados:")
print(df_carrinhos.head())
