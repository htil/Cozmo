# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:18:14 2018

@author: William Egbert
Python 3.6
"""

import socket
import cozmo

TCP_IP = '127.0.0.1'
TCP_PORT = 12345
BUFFER_SIZE = 10  # Normally 1024, but we want fast response
l = ""
print(TCP_IP)
def cozmo_program(robot: cozmo.robot.Robot):
        
        robot.say_text(l, use_cozmo_voice=False).wait_for_completed()
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while (True):
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    say = data.decode("utf-8")
    if (say != " "):
        l += say
#        print('running')
    else:
        l +=(" ")
        cozmo.run_program(cozmo_program)
        
        
    
    conn.send(data)  # echo
conn.close()




    


