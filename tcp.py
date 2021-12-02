import socket
import sys


def main():
    try:
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro:
        print(f'A conexão falhou.\nErro {erro}')
        sys.exit()

    print('Socket criado com sucesso')
    host_alvo = input('Digite o host ou ip a ser conectado: ')
    porta_alvo = input('Digite a porta a ser conectado: ')

    try:
        conexao.connect((host_alvo, int(porta_alvo)))
        print(f'Cliente TCP conectado com sucesso.\nHost: {host_alvo}\nPorta: {porta_alvo}')
        conexao.shutdown(2)
    except socket.error as erro:
        print(f'Conexão ao Host: {host_alvo} na Porta: {porta_alvo} falhou. Código do erro: {erro}')
        sys.exit()


if __name__ == '__main__':
    main()
