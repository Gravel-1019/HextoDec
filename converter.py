import socket
import json
port_receive = None
port_send = None
host = None
def parsing_json():
    with open("conf.json",mode='rt',encoding='utf-8')as f:
        conf_dic = json.loads(f.read())
        global port_send,port_receive,host
        port_send = int(conf_dic["send_port"])
        port_receive = int(conf_dic["recv_port"])
        host = conf_dic["send_host"]
def convert_hex_to_decimal(hex_data):
    decimal_list = []
    hex_values = hex_data
    for hex_value in hex_values:
        decimal_list.append(str(int(hex_value, 16)))
    return ','.join(decimal_list)



def send_data(data, host, port):
    # 创建 socket 对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # 发送数据
        client_socket.sendto(data.encode(), (host, port))
        print(f"Sent converted data: {data}")

    except Exception as e:
        print(f"Error sending data: {e}")
    finally:
        # 关闭 socket 连接
        client_socket.close()


def convert_and_send(host="localhost", port_receive=2001, port_send=2000):
    # 创建 socket 对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # 绑定主机和端口
        server_socket.bind((host, port_receive))

        print(f"Converter is listening on {host}:{port_receive}...")

        while True:
            # 接收数据
            data, addr = server_socket.recvfrom(1024)
            hex_data = data.decode().strip().split(" ")


            decimal_data = convert_hex_to_decimal(hex_data)
            send_data(decimal_data, 'localhost', port_send)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # 关闭连接
        server_socket.close()


if __name__ == "__main__":
    try:
        parsing_json()
    except FileNotFoundError:
        print("未在同级目录下检测到配置文件，请使用config_creater.py配置文件")

    convert_and_send(host, port_receive, port_send)

