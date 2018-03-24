# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 18:22:51 2018

@author: Student
"""

import websockets
import asyncio
import cozmo

#TCP_IP = socket.gethostbyname(socket.gethostname())
TCP_PORT = 12345

msg = ""
def cozmo_program(robot: cozmo.robot.Robot):
    global msg
    print(msg)
    robot.say_text(msg, use_cozmo_voice=True, duration_scalar=0.5).wait_for_completed()

async def hand(websocket, path):
    global msg
    while True:
        msg = await websocket.recv()
        print(msg)
        if msg != "":
            cozmo.run_program(cozmo_program)
    
    await websocket.send(msg)
    
start_server = websockets.serve(hand, 'localhost', TCP_PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
