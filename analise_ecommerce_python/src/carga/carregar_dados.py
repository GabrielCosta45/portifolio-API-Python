import os
import sqlite3
import requests

def carregar_dados_api():
    # Caminho simples: mesmo diretório onde está o script carregar_dados.py
    db_path = os.path.join(os.path.dirname(__file__), 'loja.db')

    # Conectar ao banco
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Criar as tabelas se não existirem (importante)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id_produto INTEGER PRIMARY KEY,
            nome_produto TEXT,
            preco REAL,
            categoria TEXT,
            avaliar REAL,
            contar INTEGER,
            descricao TEXT
        )
    ''')

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
            latitude REAL,
            longitude REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carrinhos (
            id_carrinho INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            id_produto INTEGER,
            quantidade INTEGER,
            data_criacao DATE,
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario),
            FOREIGN KEY (id_produto) REFERENCES produtos (id_produto)
        )
    ''')

    # Endpoints da API
    url_produtos = "https://fakestoreapi.com/products"
    url_usuarios = "https://fakestoreapi.com/users"
    url_carrinhos = "https://fakestoreapi.com/carts"

    # Buscar dados
    produtos = requests.get(url_produtos).json()
    usuarios = requests.get(url_usuarios).json()
    carrinhos = requests.get(url_carrinhos).json()

    # Inserir produtos
    for produto in produtos:
        cursor.execute('''
            INSERT OR IGNORE INTO produtos (id_produto, nome_produto, preco, categoria, avaliar, contar, descricao)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            produto.get('id'),
            produto.get('title'),
            produto.get('price'),
            produto.get('category'),
            produto.get('rating', {}).get('rate'),
            produto.get('rating', {}).get('count'),
            produto.get('description')
        ))

    # Inserir usuários
    for usuario in usuarios:
        endereco = usuario.get('address', {})
        geo = endereco.get('geolocation', {})

        cursor.execute('''
            INSERT OR IGNORE INTO usuarios (id_usuario, nome_completo, usuario, senha, e_mail, telefone, rua, numero, cidade, cep, latitude, longitude)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            usuario.get('id'),
            f"{usuario.get('name', {}).get('firstname', '')} {usuario.get('name', {}).get('lastname', '')}",
            usuario.get('username'),
            usuario.get('password'),
            usuario.get('email'),
            usuario.get('phone'),
            endereco.get('street'),
            str(endereco.get('number')),
            endereco.get('city'),
            endereco.get('zipcode'),
            float(geo.get('lat', 0)),
            float(geo.get('long', 0))
        ))

    # Inserir carrinhos
    for carrinho in carrinhos:
        user_id = carrinho.get('userId')
        data_carrinho = carrinho.get('date')
        produtos_carrinho = carrinho.get('products', [])

        for produto in produtos_carrinho:
            cursor.execute('''
                INSERT INTO carrinhos (id_usuario, id_produto, quantidade, data_criacao)
                VALUES (?, ?, ?, ?)
            ''', (
                user_id,
                produto.get('productId'),
                produto.get('quantity'),
                data_carrinho
            ))

    conn.commit()
    conn.close()

    print("✅ Dados carregados com sucesso!")

if __name__ == "__main__":
    carregar_dados_api()
