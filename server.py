#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
address = ('127.0.0.1',2222)

sock = socket.socket()
sock.bind(address)

sock.listen(10)
#print('Listening at address', address[0], 'port:', address[1])

while True:
   conn, addr = sock.accept()
#   print('connected:', addr)
   
   while True:
      data = bytearray(1024)
      conn.recvfrom_into(data)
      udata = data.decode('utf-8').strip('\x00')

      if udata:
#         print(udata)
         if udata == 'close': 
            conn.close()
#            print('Connection closed')
            break
         conn.send(data)
   
