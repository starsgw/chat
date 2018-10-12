# # flag=False
# # #
# # # n=None
# # # def a():
# # #
# # #     flag=True
# # #     if flag==True:
# # #         global n
# # #         n=2
# # #         return 1
# # #
# # # a()
# # # k=a()
# # # print(k)
# # # print(n)
# import socket
# import threading
# list=[[],[],[],[]]
#
#
# def srecv(s,name,index):
#     while True:
#         #一旦收到这个线程发出的任何消息，
#         # 就给出了这个线程之外的所有线程发送
#         str=s.recv(1024).decode("utf-8")
#         print(str)
#         for ss in list[index]:
#             if ss!=s:
#                 ss.send((name+":"+str).encode("utf-8"))
#
# if __name__=="__main__":
#     server=socket.socket()
#     server.bind(("localhost",8888))
#     server.listen(50)
#     while True:
#         s,addrs=server.accept()
#         name=s.recv(1024).decode("utf-8")
#         index=int(s.recv(1024).decode("utf-8"))-1
#         list[index].append(s)
#         threading.Thread(target=srecv,args=(s,name,index,)).start()
# wwb 11:16:55
# import socket
# import  threading
#
# list=[[],[],[],[]]
#
# def srecv(s,name,index):
#     while True:
#             str=(name+":"+s.recv(1024).decode("utf-8")).encode("utf-8")
#             for ss in list[index]:
#                 if ss !=s:
#                       ss.send(str)
#
#
# if __name__=="__main__":
#     server = socket.socket()
#     server.bind(('192.168.10.133', 8888))
#     server.listen(50)
#     while True:
#         s,addr=server.accept()
#         index=int(s.recv(1024).decode("utf-8"))-1
#         list[index].append(s)
#         name=s.recv(1024).decode("utf-8")
#         threading.Thread(target=srecv,args=(s,name,index,)).start()



# from qcloudsms_py import SmsSingleSender
# from qcloudsms_py.httpclient import HTTPError
# import random
# class usercheck:
#     def Check(self,phonenum):
#         appid=1400122085
#         appkey='9fbbf9cc9d1bf428a442ed15c3c9f1c9'
#         ssender = SmsSingleSender(appid, appkey)
#         key=""
#         for  i in range(1,7):
#             key+=str(random.randrange(10))
#         params = [key,5]
#
#         try:
#             result = ssender.send_with_param(86, phonenum,169389, params)
#         except HTTPError as e:
#             print(e)
#         except Exception as e:
#             print(e)
#
#         return key
# import socket
# import threading
# import re
#
# list=[[],[],[],[]]
#
# def srecv(s,name,index,nickname):
#     while True:
#             # str=(name+":"+s.recv(1024).decode("utf-8")).encode("utf-8")
#             # for ss in list[index]:
#             #     if ss !=s:
#             #           ss.send(str)
#             str = s.recv(1024).decode("utf-8")
#             if re.match("^/r nickname.",str)!=None:
#                 nickname.send((name + ":" + str).encode("utf-8"))
#             else:
#                 print(str)
#                 for ss in list[index]:
#                     if ss != s:
#                         ss.send((name + ":" + str).encode("utf-8"))
#
#
# if __name__=="__main__":
#     server = socket.socket()
#     server.bind(('192.168.10.133', 8888))
#     server.listen(50)
#     while True:
#         s,addr=server.accept()
#         name = s.recv(1024).decode("utf-8")
#         index=int(s.recv(1024).decode("utf-8"))-1
#         list[index].append(s)
#         threading.Thread(target=srecv,args=(s,name,index,)).start()
#
# import socket
# import threading
# import re
#
# list=[[],[],[],[]]
#
# def srecv(s,name,index):
#     while True:
#             # str=(name+":"+s.recv(1024).decode("utf-8")).encode("utf-8")
#             # for ss in list[index]:
#             #     if ss !=s:
#             #           ss.send(str)
#             str = s.recv(1024).decode("utf-8")
#             if re.match("^/r nickname.",str)!=None:
#                 for ss in list[index]:
#                     if ss=="nickname":
#                         ss.send((name + ":" + str[3:]).encode("utf-8"))
#             else:
#                 print(str)
#                 for ss in list[index]:
#                     if ss != s:
#                         ss.send((name + ":" + str).encode("utf-8"))
#
#
# if __name__=="__main__":
#     server = socket.socket()
#     server.bind(('192.168.10.133', 8888))
#     server.listen(50)
#     while True:
#         s,addr=server.accept()
#         name = s.recv(1024).decode("utf-8")
#         index=int(s.recv(1024).decode("utf-8"))-1
#         list[index].append(s)
#         threading.Thread(target=srecv,args=(s,name,index,)).start()
# #
# #
# import re
# str="1"
# print(re.search("1",str).span())
#
# str="1232弱智13213智障哈哈小学生哈"
# list=['弱智','小学生','智障']
#
# for s in list:
#     # if re.search(s,str)!=None:
#         s,e=re.match(s,str).span()
#         str=str[:s]+"**"+str[e:]
#
# print(str)


import socket
import threading
import re

list=[[],[],[],[]]

def srecv(s,name,index):
    while True:
            # str=(name+":"+s.recv(1024).decode("utf-8")).encode("utf-8")
            # for ss in list[index]:
            #     if ss !=s:
            #           ss.send(str)
            str = s.recv(1024).decode("utf-8")
            if re.match("^/r nickname.",str)!=None:
                for ss in list[index]:
                    if ss=="nickname":
                        ss.send((name + ":" + str).encode("utf-8"))
            else:
                print(str)
                for ss in list[index]:
                    if ss != s:
                        ss.send((name + ":" + str).encode("utf-8"))


if __name__=="__main__":
    server = socket.socket()
    server.bind(('192.168.10.133', 8888))
    server.listen(50)
    while True:
        s,addr=server.accept()
        name = s.recv(1024).decode("utf-8")
        index=int(s.recv(1024).decode("utf-8"))-1
        list[index].append(s)
        threading.Thread(target=srecv,args=(s,name,index,)).start()
