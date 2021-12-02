import socket


def main():
    conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket criado com sucesso')

    host = 'localhost'
    porta = 5432

    conexao.bind((host, porta))
    mensagem = '\nServidor: Hello World'

    while 1:
        dados, end = conexao.recvfrom(4096)

        if dados:
            print('Servidor enviando mensagem...')
            conexao.sendto(dados + (mensagem.encode()), end)


if __name__ == '__main__':
    main()
