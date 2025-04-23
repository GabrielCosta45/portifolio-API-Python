import requests
import pandas as pd

# 🔹 Etapa 1

# ✅ Escolher uma API

# ✅ Fazer a extração de pelo menos 3 tabelas 



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

df_produtos.rename(columns={'id': 'id_produto', 'title': 'nome_produto', 'price': 'preco'}, inplace=True)
df_produtos['preco'] = df_produtos['preco'].astype(float)

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


# 🔹 Etapa 2

# ✅ Realizar os tratamentos devidos das tabelas

# TABELA DE PRODUTOS

df_produtos.rename(columns={'id': 'id_produto', 'title': 'nome_produto', 'price': 'preco', 'description': 'descricao', 'category': 'categoria', 'image': 'imagem', 'rating': 'avaliacao'}, inplace=True)
df_produtos['preco'] = df_produtos['preco'].astype(float)
df_produtos['id_produto'] = df_produtos['id_produto'].astype(int)
df_produtos['nome_produto'] = df_produtos['nome_produto'].astype(str)
df_produtos['descricao'] = df_produtos['descricao'].astype(str)
df_produtos['categoria'] = df_produtos['categoria'].astype(str)


df_produtos.head(5)


# TABELA DE USUÁRIOS

df_usuarios.rename(columns={
    'name': 'nome',
    'address': 'endereco',

    'id': 'id_produto',
    'email': 'e-mail',
    'username': 'usuario',
    'password': 'senha',
    'phone': 'telefone'
}, inplace=True)

# Criar coluna 'nome_completo' se a coluna 'nome' existir
if 'nome' in df_usuarios.columns:
    df_usuarios['nome_completo'] = df_usuarios['nome'].apply(
        lambda x: f"{x['firstname']} {x['lastname']}" if isinstance(x, dict) else ''
    )

# Extrair informações de endereço
if 'endereco' in df_usuarios.columns:
    # Extrair rua, cidade, número e CEP
    df_usuarios['rua'] = df_usuarios['endereco'].apply(
        lambda x: x['street'] if isinstance(x, dict) and 'street' in x else ''
    )
    df_usuarios['cidade'] = df_usuarios['endereco'].apply(
        lambda x: x['city'] if isinstance(x, dict) and 'city' in x else ''
    )
    df_usuarios['numero'] = df_usuarios['endereco'].apply(
        lambda x: x['number'] if isinstance(x, dict) and 'number' in x else ''
    )
    df_usuarios['cep'] = df_usuarios['endereco'].apply(
        lambda x: x['zipcode'] if isinstance(x, dict) and 'zipcode' in x else ''
    )

    # Extrair latitude e longitude
    df_usuarios['latitude'] = df_usuarios['endereco'].apply(
        lambda x: x['geolocation']['lat'] if isinstance(x, dict) and 'geolocation' in x else ''
    )
    df_usuarios['longitude'] = df_usuarios['endereco'].apply(
        lambda x: x['geolocation']['long'] if isinstance(x, dict) and 'geolocation' in x else ''
    )


    df_usuarios.drop(columns=['endereco'], inplace=True)







    
# Visualizar os primeiros registros
df_usuarios.head(5)
