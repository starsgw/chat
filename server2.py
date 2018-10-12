import socket
import threading
import re
#
# listkx=[]#走近科学
# list1sj=[]#动物世界
list=[[],[]]

def srecv(s,name,change):
    # if change == "1":  # 判断选择的聊天室
    #     list=listkx
    # elif change == "2":
    #     list=list1sj
    while True:
        str=(s.recv(1024).decode('utf-8'))
        # for ss in list[change]:
        #     str1="^r/"+ss
        if str=="r/":
        # if re.search("r/", str).span()!=None:

            a, b = re.search(" r/", str).span()
            one = str[b]
            one.send((name + ":" + str).encode("utf-8"))
            break
            # if re.search(" r/", str).span() != None:
            # for ss in list[change]:
                # if "n"==ss:
                # ss.send((name+":"+str).encode("utf-8"))
        else:
            for ss in list[change]:
                if ss != s:
                    ss.send((name+":"+str).encode("utf-8"))

        # if re.search("^\r n", str) != None:
        #     for ss in list[change]:
        #         if ss=="n":
        #             ss.send()
        # else:
        #     for ss in list[change]:
        #         if ss != s:
        #             ss.send(str)

if __name__=='__main__':
    server=socket.socket()
    server.bind(('localhost', 8888))
    server.listen(50)
    while True:
        s,addr = server.accept()
        name = s.recv(1024).decode('utf-8')
        change = int(s.recv(1024).decode('utf-8')) - 1  # change减一等于下标
        list[change].append(s)
        # change.append(s)
        threading.Thread(target=srecv,args=(s,name,change,)).start()

