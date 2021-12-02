import socket


def main():
    conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Cliente Socket criado com sucesso')

    host = 'localhost'
    porta = 5433
    mensagem = 'Hello World'

    try:
        print(f'Cliente: {mensagem}')
        conexao.sendto(mensagem.encode(), (host, 5432))
        dados, servidor = conexao.recvfrom(4096)
        dados = dados.decode()
        print(f"Cliente: {dados}")
    finally:
        print('Cliente: Encerrando conexão')
        conexao.close()


if __name__ == '__main__':
    main()
