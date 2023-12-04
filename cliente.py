# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:28:33 2015

@author: mag
"""

import socket

miSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
miSocket.connect( (socket.gethostname(), 4545 ) )
while True:
    mensaje_enviar = input("Cliente: ")
    miSocket.send(mensaje_enviar.encode('utf-8'))
    mensaje_recibido = miSocket.recv(100).decode('utf-8')
    print("Servidor:", mensaje_recibido)
    if mensaje_enviar.lower() == 'bye':
        break
miSocket.close()