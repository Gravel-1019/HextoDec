import socket


def receive_data(host, port):
    # 创建 socket 对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # 绑定主机和端口
        server_socket.bind((host, port))

        print(f"Receiver is listening on {host}:{port}...")

        while True:
            # 接收数据
            data, addr = server_socket.recvfrom(1024)
            print(f"Received data: {data.decode()} from {addr}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # 关闭连接
        server_socket.close()


if __name__ == "__main__":
    receive_data('localhost', 2000)

