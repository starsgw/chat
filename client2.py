import socket
import threading
import os

change=None
list0=[]
# class Client(object):
# def client(name,change):
#     s=socket.socket()
#     s.connect(('localhost',8888))
#     s.send(name.encode("utf-8"))
#     s.send(change.encode("utf-8"))
#     return s#name返回给s=c.client()
def namechek():
    # list0=[]
    global list0
    path=r'E:\user'
    usernamelist=[name[:-4] for name in os.listdir(path)]
    for username in usernamelist:
        file0=open(path+"\\"+username+".txt","r+")
        name = file0.read().split(" ")[1]
        list0.append(name)
        file0.close()

def login():
    path=r'E:\user'
    username=input("请输入账号：")
    usernamelist=[name[:-4] for name in os.listdir(path)]
    if username not in usernamelist:
        print("此用户不存在")
        login()
    else:
        password1=input("请输入密码：")
        file=open(path+"\\"+username+".txt","r+")
        password=file.read().split(" ")[0]
        if password1==password:
            print("登录成功")

            # global change
            # key1=input("请选择聊天室：1.走近科学  2.动物世界\n")
            # change=key1

            file.close()#再次读值需先关闭后打开
            file1=open(path+"\\"+username+".txt","r+")
            return file1.read().split(" ")[1]#name返回给name=c.login()
        else:
            print("密码不正确")
            login()

def regist():
    namechek()
    path=r"E:\user"
    usernamelist = [name[:-4] for name in os.listdir(path)]
    username=input("请输入账号：")
    if username not in usernamelist:
        password=input("请输入密码：")
        name=input("请输入昵称：")
        if name not in list0:
            file=open(path+'\\'+username+'.txt',"w+")
            file.write(password+" "+name)
            file.close()
            index()
        else:
            print("此昵称已被占用")
            regist()
    else:
        print("此账号已注册")
        regist()

def csend(s):
    while True:
        str=input().encode("utf-8")
        s.send(str)

def crecv(s):
    while True:
        print(s.recv(1024).decode("utf-8"))

def index():
    name = login()
    key1 = input("请选择聊天室：1.走近科学  2.动物世界\n")
    change = key1
    s.send(name.encode("utf-8"))
    s.send(change.encode("utf-8"))

if __name__=="__main__":
    # c=Client()
    s = socket.socket()
    s.connect(('localhost', 8888))

    key=input("1登录  2注册")
    if key=="1":
        name=login()
        # global change
        key1 = input("请选择聊天室：1.走近科学  2.动物世界\n")
        change = key1
        # s=client(name,change)
        s.send(name.encode("utf-8"))
        s.send(change.encode("utf-8"))
    elif key=="2":
        regist()
    threading.Thread(target=csend,args=(s,)).start()#发出的消息，由参数s传内容
    threading.Thread(target=crecv,args=(s,)).start()#收到的消息

