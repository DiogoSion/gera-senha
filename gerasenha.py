import secrets
import string


def gerar_senha(tam):
    """
        Gera uma senha forte com letras, números e caracteres especiais.

        Args:
            tam (int):O comprimento desejado da senha.

        Returns:
            str: A senha forte gerada.
    """
    letras = string.ascii_letters
    digitos = string.digits
    especiais = string.punctuation

    caracteres = letras + digitos + especiais

    senha_forte = False
    senha = ""

    while not senha_forte:
        senha = ''.join(secrets.choice(caracteres) for _ in range(tam))

        # Critérios para uma senha forte, nesse caso pelo menos 1 caracter especial e 1 número
        if (any(char in especiais for char in senha) and
                sum(char in digitos for char in senha)):
            senha_forte = True

    return senha


if __name__ == '__main__':

    while True:
        try:
            tamanho_senha = int(input("Digite o tamanho desejado da senha: "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    senha_gerada = gerar_senha(tamanho_senha)
    print(f"Sua senha forte: {senha_gerada}")
