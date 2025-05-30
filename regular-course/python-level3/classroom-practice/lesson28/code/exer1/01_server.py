import json
import socket
import threading


class Message:
    def __init__(self, cmd, content, sender, to=None):
        self.cmd = cmd
        self.content = content
        self.sender = sender
        self.to = to


class Server:

    def __init__(self, ip, port):
        self.socket = socket.socket()
        self.socket.bind((ip, port))
        self.socket.listen()
        self.connSockets = {}
        self.avatars = {}

    def sendMsg(self, connSocket, msg, code):
        print('发送消息：', {'code': code, 'msg': msg.__dict__})
        msg = json.dumps({'code': code, 'msg': msg.__dict__})
        connSocket.send(msg.encode())

    def recvMsg(self, connSocket):
        try:
            req = connSocket.recv(1024 * 1000).decode()
            req = json.loads(req)
            return req
        except Exception as e:
            print(e)

    def run(self):
        while True:
            print('等待连接...')
            connSocket, clientAddr = self.socket.accept()
            t = threading.Thread(target=self.handle, args=[connSocket])
            t.start()

    def handle(self, connSocket):
        while True:
            req = self.recvMsg(connSocket)
            print('接收到的消息：', req)
            if not req:
                break
            if req['cmd'] == 'login':
                self.login(connSocket, req)
            elif req['cmd'] == 'chat':
                self.chat(req)
            # 4. 如果req的cmd键的值等于video，则调用video方法

        self.quit(connSocket)

    # 1. 定义video方法和req参数，实现视频聊天

    # 2. 获取req的to键的值，保存到变量to中

    # 3. 把req转换为Message对象msg，并转发消息msg给to

    def chat(self, req):
        to = req['to']
        if req['sender'] != to:
            msg = Message(**req)
            self.sendMsg(self.connSockets[to], msg, 200)

    def quit(self, connSocket):
        connSocket.close()
        for name, cSocket in self.connSockets.items():
            if connSocket == cSocket:
                del self.connSockets[name]
                del self.avatars[name]
                msg = Message('quit', name, '服务器')
                for cSocket in self.connSockets.values():
                    self.sendMsg(cSocket, msg, 200)
                break

    def login(self, connSocket, req):
        sender = req['sender']
        if sender in self.connSockets:
            msg = Message('login', '该账号已登录', '服务器')
            self.sendMsg(connSocket, msg, 401)
            return
        msg = Message(**req)
        for cSocket in self.connSockets.values():
            self.sendMsg(cSocket, msg, 200)
        self.connSockets[sender] = connSocket
        self.avatars[sender] = req['content']
        print(self.connSockets)
        print(self.avatars)
        msg = Message(req['cmd'], self.avatars, '服务器')
        self.sendMsg(connSocket, msg, 200)


if __name__ == '__main__':
    server = Server('0.0.0.0', 10101)
    server.run()
