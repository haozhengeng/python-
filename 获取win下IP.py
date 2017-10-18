import socket, threading
from time import ctime

# 定义相关环境变量
BUFSIZ = 1024
# 主机IP
HOST = "localhost"
# 主机端口
PORT = 20000
# 合成地址
ADDR = (HOST, PORT)

# 接收消息相关方法属性
recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_socket.bind(('', PORT))


def recv_func():
    while True:
        data, addr = recv_socket.recvfrom(BUFSIZ)
        r_str = data.decode("utf-8")
        print("         recv:%s" % r_str)
        if r_str == "exit":
            print("thread-----down")
            break



def main():
    # 创建接受消息线程
    recv_t = threading.Thread(target=recv_func)
    recv_t.start()
    # 创建发送消息循环
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        msg = input(">")
        if msg == "exit":
            send_socket.sendto(msg.encode("utf-8"), ADDR)
            break
        send_socket.sendto(msg.encode("utf-8"), ADDR)

    send_socket.close()
    recv_t.join()
    recv_socket.close()


if __name__ == '__main__':
    main()
