## 🔹 ETAPA 5 - SISTEMA DE ALERTA

# ✅ Alerta, caso o usuario faça um registro sem o e_mail cadastrado

from plyer import notification

def notificar_usuario(e_mail, df_usuarios):
    # Verifica se o e-mail foi fornecido
    if not e_mail or not isinstance(e_mail, str):
        print("Erro: E-mail inválido ou vazio.")
        return

    # Verifica se a coluna 'e_mail' existe no DataFrame
    if 'e_mail' not in df_usuarios.columns:
        print("Erro: A coluna 'e_mail' não existe no DataFrame.")
        return

    # Verifica se o e-mail está cadastrado
    if e_mail in df_usuarios['e_mail'].values:
        print(f"E-mail '{e_mail}' encontrado na base de dados.")
    else:
        print(f"E-mail '{e_mail}' NÃO encontrado na base de dados. Notificando...")
        notification.notify(
            title='Alerta de Notificação',
            message=f'Atenção! O e-mail "{e_mail}" não está cadastrado!',
            app_name='Loja Fake Store',
            timeout=10
        )


from plyer import notification

def notificar_usuario(e_mail, df_usuarios):
    # Verifica se o e-mail foi fornecido
    if not e_mail or not isinstance(e_mail, str):
        print("Erro: E-mail inválido ou vazio.")
        return

    # Verifica se a coluna 'e_mail' existe no DataFrame
    if 'e_mail' not in df_usuarios.columns:
        print("Erro: A coluna 'e_mail' não existe no DataFrame.")
        return

    # Verifica se o e-mail está cadastrado
    if e_mail in df_usuarios['e_mail'].values:
        print(f"E-mail '{e_mail}' encontrado na base de dados.")
    else:
        print(f"E-mail '{e_mail}' NÃO encontrado na base de dados. Notificando...")
        notification.notify(
            title='Alerta de Notificação',
            message=f'Atenção! O e-mail "{e_mail}" não está cadastrado!',
            app_name='Loja Fake Store',
            timeout=10
        )


# Exemplo de uso

import pandas as pd

# Exemplo de uso, voce pode alterar o e-mail para testar
df_usuarios = pd.DataFrame({'e_mail': ['don@gmail.com']}
)

notificar_usuario('don@gmail.com', df_usuarios)

