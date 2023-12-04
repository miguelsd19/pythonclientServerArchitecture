# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:29:55 2015

@author: mag
"""

import socket
puerto = 4545;
miSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
miSocket.bind( ( socket.gethostname(), puerto ) )
miSocket.listen( 1 )
while True:
    channel, details = miSocket.accept()
    print("Conexión establecida desde", details)
    while True:
        mensaje_recibido = channel.recv(100).decode('utf-8')
        print("Cliente:", mensaje_recibido)
        mensaje_enviar = input("Servidor: ")
        channel.send(mensaje_enviar.encode('utf-8'))
        if mensaje_enviar.lower() == 'bye':
            break
    channel.close()