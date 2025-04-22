import requests
import pandas as pd

# URLs da API
url_produto = 'https://fakestoreapi.com/products'
url_usuarios = 'https://fakestoreapi.com/users'
url_carrinhos = 'https://fakestoreapi.com/carts'

# Requisição para os produtos
res_produtos = requests.get(url_produto)
if res_produtos.status_code == 200:
    df_produtos = pd.DataFrame(res_produtos.json())
    print("Tabela de Produtos")
    print(df_produtos.head(5))
else:
    print(f"Erro ao acessar produtos: {res_produtos.status_code}")

# Requisição para os usuários
res_usuarios = requests.get(url_usuarios)
if res_usuarios.status_code == 200:
    df_usuarios = pd.DataFrame(res_usuarios.json())
    print("Tabela de Usuários")
    print(df_usuarios.head(5))
else:
    print(f"Erro ao acessar usuários: {res_usuarios.status_code}")

# Requisição para os carrinhos
res_carrinhos = requests.get(url_carrinhos)
if res_carrinhos.status_code == 200:
    df_carrinhos = pd.DataFrame(res_carrinhos.json())
    print("Tabela de Carrinhos")
    print(df_carrinhos.head(5))
else:
    print(f"Erro ao acessar carrinhos: {res_carrinhos.status_code}")
