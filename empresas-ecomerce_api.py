import requests
import pandas as pd

# Função de alerta
def alerta(msg):
    print(f"🚨 ALERTA: {msg}")

# Função para consultar dados via CNPJ
def consultar_cnpj(cnpj):
    url = f'https://brasilapi.com.br/api/cnpj/v1/{cnpj}'
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as e:
        alerta(f"Erro ao consultar CNPJ {cnpj}: {e}")
        return None

# Função para extrair tabelas
def extrair_tabelas(dados_empresas):
    # Tabela 1 - Informações básicas
    tabela_basica = pd.DataFrame([{
        'Nome Fantasia': d.get('nome_fantasia'),
        'Razão Social': d.get('razao_social'),
        'CNPJ': d.get('cnpj'),
        'Tipo': d.get('tipo'),
        'Situação': d.get('descricao_situacao_cadastral')
    } for d in dados_empresas])
    print("\n✅ Tabela 1 - Informações Básicas")
    print(tabela_basica)

    # Tabela 2 - Endereços
    tabela_endereco = pd.DataFrame([{
        'CNPJ': d.get('cnpj'),
        'UF': d.get('uf'),
        'Cidade': d.get('municipio'),
        'Bairro': d.get('bairro'),
        'Logradouro': d.get('logradouro'),
        'Número': d.get('numero')
    } for d in dados_empresas])
    print("\n✅ Tabela 2 - Endereços")
    print(tabela_endereco)

    # Tabela 3 - CNAEs Secundários
    todas_cnaes = []
    for d in dados_empresas:
        for cnae in d.get('cnaes_secundarios', []):
            todas_cnaes.append({
                'CNPJ': d.get('cnpj'),
                'CNAE': cnae.get('codigo'),
                'Descrição': cnae.get('descricao')
            })
    tabela_cnaes = pd.DataFrame(todas_cnaes)
    print("\n✅ Tabela 3 - Atividades Econômicas (CNAEs)")
    print(tabela_cnaes)

# Função principal
def main():
    cnpjs = ['07526557000100', '60746948000112', '61186680000174']  # AMBEV S/A, Banco Bradesco S.A, Banco BMG S.A.
    dados_empresas = []

    for cnpj in cnpjs:
        dados = consultar_cnpj(cnpj)
        if dados:
            dados_empresas.append(dados)

    if dados_empresas:
        extrair_tabelas(dados_empresas)
    else:
        alerta("Nenhum dado de empresa foi carregado.")

if __name__ == "__main__":
    main()
