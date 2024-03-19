import socket
import random


def generate_hex_data(length):
    hex_data = ''.join(random.choice('0123456789ABCDEF') for _ in range(length))
    # 将每两位十六进制数据以空格分开
    hex_data_spaced = ' '.join(hex_data[i:i+2] for i in range(0, len(hex_data), 2))
    return hex_data_spaced



def send_data(hex_data, host, port):
    # 创建 socket 对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # 发送数据
        client_socket.sendto(hex_data.encode(), (host, port))
        print(f"Sent hex data: {hex_data}")

    except Exception as e:
        print(f"Error sending data: {e}")
    finally:
        # 关闭 socket 连接
        client_socket.close()


if __name__ == "__main__":
    hex_data = generate_hex_data(10)  # 生成长度为10的16进制数据
    print(f"Generated hex data: {hex_data}")
    send_data(hex_data, 'localhost', 2001)  # 发送到converter的2001端口


