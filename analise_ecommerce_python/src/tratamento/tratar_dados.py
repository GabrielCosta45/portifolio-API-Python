import pandas as pd

def tratar_produtos(df_produtos):
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

    df_produtos['preco'] = df_produtos['preco'].astype(float)
    df_produtos['id_produto'] = df_produtos['id_produto'].astype(int)
    df_produtos.drop(columns=['imagem', 'avaliacao'], inplace=True)

    df_produtos = df_produtos[[
        'id_produto', 'nome_produto', 'preco', 
        'categoria', 'avaliar', 'contar', 'descricao'
    ]]

    return df_produtos


def tratar_usuarios(df_usuarios):
    df_usuarios.rename(columns={
        'name': 'nome',
        'address': 'endereco',
        'id': 'id_usuario',
        'email': 'e_mail',
        'username': 'usuario',
        'password': 'senha',
        'phone': 'telefone'
    }, inplace=True)

    if 'nome' in df_usuarios.columns:
        df_usuarios['nome_completo'] = df_usuarios['nome'].apply(
            lambda x: f"{x['firstname']} {x['lastname']}" if isinstance(x, dict) else ''
        )

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
        df_usuarios['latitude'] = df_usuarios['endereco'].apply(
            lambda x: x['geolocation']['lat'] if isinstance(x, dict) and 'geolocation' in x else ''
        )
        df_usuarios['longitude'] = df_usuarios['endereco'].apply(
            lambda x: x['geolocation']['long'] if isinstance(x, dict) and 'geolocation' in x else ''
        )

    df_usuarios['latitude'] = df_usuarios['latitude'].astype(float)
    df_usuarios['longitude'] = df_usuarios['longitude'].astype(float)

    df_usuarios.drop(columns=['endereco', 'nome', '__v'], inplace=True)

    df_usuarios = df_usuarios[[
        'id_usuario', 'nome_completo', 'usuario', 'senha', 'e_mail',
        'telefone', 'rua', 'numero', 'cidade', 'cep', 'latitude', 'longitude'
    ]]

    return df_usuarios


def tratar_carrinhos(df_carrinhos):
    df_carrinhos.rename(columns={
        'id': 'id_carrinho',
        'userId': 'id_usuario',
        'products': 'produtos',
        'date': 'data_criacao',
    }, inplace=True)

    df_carrinhos['data_criacao'] = pd.to_datetime(df_carrinhos['data_criacao'])
    df_carrinhos.drop(columns=['__v'], inplace=True)

    df_carrinhos['produtos'] = df_carrinhos['produtos'].apply(lambda x: x if isinstance(x, list) else [])
    df_carrinhos = df_carrinhos.explode('produtos').reset_index(drop=True)

    df_carrinhos['id_produto'] = df_carrinhos['produtos'].apply(
        lambda x: x['productId'] if isinstance(x, dict) and 'productId' in x else None
    )

    df_carrinhos['quantidade'] = df_carrinhos['produtos'].apply(
        lambda x: x['quantity'] if isinstance(x, dict) and 'quantity' in x else None
    )

    df_carrinhos = df_carrinhos[[
        'id_carrinho', 'id_usuario', 'id_produto', 'quantidade', 'data_criacao'
    ]]

    return df_carrinhos
