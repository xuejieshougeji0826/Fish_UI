import sys,socket,time
from PyQt5.QtWidgets import QApplication, QMainWindow
from fish import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtCore import QTimer
import cgitb
cgitb.enable( format ='text')
class MyMainWindow(QMainWindow, Ui_MainWindow):
    printSignal = pyqtSignal(list)
    helpSignal = pyqtSignal(str)
    def __init__( self, parent=None ):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
    def tcp_connect(self,one,two,three,four,five):
        self.HOST_IP = str(str(one)+"."+str(two)+"."+str(three)+"."+str(four))
        self.HOST_PORT = five
        # 创建Socket，SOCK_STREAM表示类型为TCP
        self.zhuangtai.append("Starting socket: TCP...")
        self.socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.zhuangtai.append("TCP server listen @ %s:%d!" % (self.HOST_IP, self.HOST_PORT))
        host_addr = (self.HOST_IP, self.HOST_PORT)
        self.socket_tcp.bind(host_addr)
        self.socket_tcp.listen(1)
        # 接受Client发出的连接请求，返回值包含了Client的IP和端口
        self.socket_con, (client_ip, client_port) = self.socket_tcp.accept()
        self.zhuangtai.append("Connection accepted from %s." % client_ip)
        # 向Clinet发送数据
        self.socket_con.send("Welcome to RPi TCP server!".encode())
        self.zhuangtai.append("succeed")
    def initUI( self ):
        self.ip_connect.clicked.connect(self.connect_to_pi)
        self.send.clicked.connect(self.send_control_Signal)
        self.save_tuoluoyi.clicked.connect(self.save_as_txt)
        self.timer = QTimer()
        self.timer.timeout.connect(self.readtuoluoyi)  # 计时器挂接到槽：update
        #self.read_tuoluoyi.clicked.connect(self.readtuoluoyi)
        self.read_tuoluoyi.clicked.connect(lambda: self.timer.start(2000))
    def save_as_txt(self):
        self.tuoluoyi_data= self.tuoluoyi.toPlainText()
        f1 = open('data.txt', 'w')
        f1.write(self.tuoluoyi_data)
        self.tuoluoyi.append("已经保存到data.txt")
    # def jieshou(self):
    #     self.data = self.socket_con.recv(15)
    #     print(str(self.data))
    #     self.timer = QTimer(self)
    #     self.timer.start(5000)
    #     self.tuoluoyi.append(str(self.data) + "\n")
    def readtuoluoyi(self):
        try:
            self.socket_con.send(b"read")
            #self.tuoluoyi.append("正在读取。。。")
            self.data = self.socket_con.recv(12)
            self.tuoluoyi.append(str(self.data))

        except:self.tuoluoyi.append("读取失败，请重新读取")
    def send_control_Signal(self):
        try:
            xq=float(self.xiongqi.text())
            self.socket_con.send(("xq"+str(xq)).encode())
            self.zhuangtai.append("胸鳍转动："+str(xq))
        except:
            self.zhuangtai.append("请重新输入")

    def connect_to_pi(self):
        try:
            ip_1= int(self.ip1.text())
            ip_2 = int(self.ip2.text())
            ip_3 = int(self.ip3.text())
            ip_4 = int(self.ip4.text())
            duankou = int(self.duankouhao.text())
            # ip_1= 172
            # ip_2 = 27
            # ip_3 = 110
            # ip_4 = 119
            # duankou=8081
            self.zhuangtai.append("要连接的树莓派的IP地址为："+str(ip_1)+"."+str(ip_2)+"."+str(ip_3)+"."
                                  +str(ip_4)+'\n'+"要连接的树莓派的端口号为："+str(duankou))
            self.zhuangtai.append("正在连接。。。")
            self.tcp_connect(ip_1,ip_2,ip_3,ip_4,duankou)
        except:
            self.zhuangtai.append("IP或端口错误请重新输入重新连接")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
    socket_tcp.close()