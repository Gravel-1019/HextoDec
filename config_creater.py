import json
def print_logo():
    logo = '''
      ____                    __   _         
     / ___|   ___    _ __    / _| (_)   __ _ 
    | |      / _ \  | '_ \  | |_  | |  / _` |
    | |___  | (_) | | | | | |  _| | | | (_| |
    \ ____|  \___/  |_| |_| |_|   |_|  \__, |
                                        |___/ 
    配置文件程序
            '''
    print("\033[92m", logo, "\033[0m")

def main():
    print("请按照引导回答问题")
    recv_port = input("输入插件的接收端口(默认2001)：")
    send_port = input("输入插件的发送端口(默认2000)：")
    send_host = input("插件的发送的IP地址(默认本机地址)：")
    conf_dict = {
        "recv_port": int(recv_port) if recv_port else 2001,
        "send_port": int(send_port) if send_port else 2000,
        "send_host": send_host if send_host else "localhost"
    }
    with open("conf.json",mode="wt",encoding='utf-8')as f:
        f.write(json.dumps(conf_dict))

if __name__ == '__main__':
    try:
        print_logo()
        main()
    except Exception as e:
        print(f"error:{e}")
