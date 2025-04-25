import requests
import pandas as pd
from numpy import dtype as np
from datetime import datetime
import sqlite3

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

####

df_produtos.rename(columns={
    'id': 'id_produto', 
    'title': 'nome_produto', 
    'price': 'preco', 
    'description': 'descricao', 
    'category': 'categoria', 
    'image': 'imagem', 
    'rating': 'avaliacao'
    }, inplace=True)


if 'avaliacao' in df_produtos.columns:

    df_produtos['avaliar'] = df_produtos['avaliacao'].apply(
        lambda x: x['rate'] if isinstance(x, dict) and 'rate' in x else None
    )
    df_produtos['contar'] = df_produtos['avaliacao'].apply(
        lambda x: x['count'] if isinstance(x, dict) and 'count' in x else None
    )
else:
    print("A coluna 'avaliacao' não está presente no DataFrame.")

# Transformar para float
df_produtos['preco'] = df_produtos['preco'].astype(float)
df_produtos['id_produto'] = df_produtos['id_produto'].astype(int)

# Remover colunas desnecessárias
df_produtos.drop(columns=['imagem'], inplace=True)
df_produtos.drop(columns=['avaliacao'], inplace=True)


df_produtos = df_produtos[['id_produto', 'nome_produto', 'preco', 'categoria', 'avaliar', 'contar', 'descricao']]

df_produtos.head(5)


####


# Renomear as colunas para nomes mais legíveis
df_usuarios.rename(columns={
    'name': 'nome',
    'address': 'endereco',
    'id': 'id_usuario',
    'email': 'e_mail',
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

# Transformar para float
df_usuarios['latitude'] = df_usuarios['latitude'].astype(float)
df_usuarios['longitude'] = df_usuarios['longitude'].astype(float)

# Remover colunas desnecessárias
df_usuarios.drop(columns=['endereco'], inplace=True)
df_usuarios.drop(columns=['nome'], inplace=True)
df_usuarios.drop(columns=['__v'], inplace=True)

# posicionar as colunas
df_usuarios = df_usuarios[['id_usuario', 'nome_completo', 'usuario', 'senha', 'e_mail', 'telefone', 'rua', 'numero', 'cidade', 'cep', 'latitude', 'longitude']]


df_usuarios.head(5)


####


# Renomear as colunas para nomes mais legíveis
df_usuarios.rename(columns={
    'name': 'nome',
    'address': 'endereco',
    'id': 'id_usuario',
    'email': 'e_mail',
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

# Transformar para float
df_usuarios['latitude'] = df_usuarios['latitude'].astype(float)
df_usuarios['longitude'] = df_usuarios['longitude'].astype(float)

# Remover colunas desnecessárias
df_usuarios.drop(columns=['endereco'], inplace=True)
df_usuarios.drop(columns=['nome'], inplace=True)
df_usuarios.drop(columns=['__v'], inplace=True)

# posicionar as colunas
df_usuarios = df_usuarios[['id_usuario', 'nome_completo', 'usuario', 'senha', 'e_mail', 'telefone', 'rua', 'numero', 'cidade', 'cep', 'latitude', 'longitude']]


df_usuarios.head(5)


####


# Renomear colunas
df_carrinhos.rename(columns={
    'id': 'id_carrinho',
    'userId': 'id_usuario',
    'products': 'produtos',
    'date': 'data_criacao',
}, inplace=True)

# Converter data
df_carrinhos['data_criacao'] = pd.to_datetime(df_carrinhos['data_criacao'])


df_carrinhos.drop(columns=['__v'], inplace=True)

# Garante que todos os valores da coluna sejam listas
df_carrinhos['produtos'] = df_carrinhos['produtos'].apply(lambda x: x if isinstance(x, list) else [])

# Explode os produtos (transforma cada produto em uma linha separada)
df_carrinhos = df_carrinhos.explode('produtos').reset_index(drop=True)

# Extrai campos de cada produto
df_carrinhos['id_produto'] = df_carrinhos['produtos'].apply(
    lambda x: x['productId'] if isinstance(x, dict) and 'productId' in x else None
)

df_carrinhos['quantidade'] = df_carrinhos['produtos'].apply(
    lambda x: x['quantity'] if isinstance(x, dict) and 'quantity' in x else None
)

df_carrinhos = df_carrinhos[['id_carrinho', 'id_usuario', 'id_produto', 'quantidade', 'data_criacao']]


df_carrinhos.head()


####


conn = sqlite3.connect('loja.db')
cursor = conn.cursor()


# Criar tabela 'produtos'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id_produto INTEGER PRIMARY KEY,
        nome_produto TEXT,
        preco float,
        categoria TEXT,
        avaliar float,
        contar INTEGER,
        descricao TEXT
    )
''')

# Criar tabela 'usuarios'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY,
        nome_completo TEXT,
        usuario TEXT,
        senha TEXT,
        e_mail TEXT,
        telefone TEXT,
        rua TEXT,
        numero TEXT,
        cidade TEXT,
        cep TEXT,
        latitude float,
        longitude float
    )
''')

# Criar tabela 'carrinhos'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS carrinhos (
        id_carrinho INTEGER PRIMARY KEY,
        id_usuario INTEGER,
        id_produto INTEGER,
        quantidade INTEGER,
        data_criacao DATE,
        FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario),
        FOREIGN KEY (id_produto) REFERENCES produtos (id_produto)
    )
''')

df_produtos.to_sql('produtos', conn, if_exists='append', index=False)
df_usuarios.to_sql('usuarios', conn, if_exists='append', index=False)
df_carrinhos.to_sql('carrinhos', conn, if_exists='replace', index=False)

conn.commit()
conn.close()

print("Dados inseridos com sucesso!")