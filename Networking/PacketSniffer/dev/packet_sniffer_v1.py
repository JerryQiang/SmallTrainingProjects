import socket


class PromiscuousSocket:
    def __init__(self):
        # 创建socket
        HOST = socket.gethostbyname(socket.gethostname())
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, 0))
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        self.s = s

    def __enter__(self):
        return self.s

    def __exit__(self, *args, **kwargs):
        self.s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)  # 关闭混杂模式

def sniffer(count, bufferSize=65565, showPort=True, showRawData=True):
    with PromiscuousSocket() as s:
        for i in range(count):
            # receive a package

            package = s.recvfrom(bufferSize)

            printPacket(package, showPort, showRawData)

def printPacket(package, showPort, showRawData):
    dataIndex = 0
    headerIndex = 1
    ipAddressIndex = 0
    portIndex = 1
    print('IP:', package[headerIndex][ipAddressIndex], end=' ')
    if (showPort):
        print('Port:', package[headerIndex][portIndex], end=' ')
    print('')  # newline
    if (showRawData):
        print('Data:', package[dataIndex])

if __name__ == '__main__':
    sniffer(100)