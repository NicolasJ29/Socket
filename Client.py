import socket
UDP_IP= "10.160.108.101"
UDP_PORT= 5005
data="4158522552"
decimal=0
idx=1
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


sock.sendto(data.encode(),(UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(4)

hexa=data
compteur=0
while (compteur<8):
    if(hexa[-compteur]=='f'):
        decimal+=15*(16**(2-(compteur+1)))
    elif(hexa[-compteur]=='e'):
        decimal+=14*(16**(2-(compteur+1)))
    elif(hexa[-compteur]=='d'):
        decimal+=13*(16**(2-(compteur+1)))
    elif(hexa[-compteur]=='c'):
        decimal+=12*(16**(2-(compteur+1)))
    elif(hexa[-compteur]=='b'):
        decimal+=11*(16**(2-(compteur+1)))
    elif(hexa[-compteur]=='a'):
        decimal+=10*(16**(2-(compteur+1)))
    else:
        valeur=int(hexa[compteur])
        decimal+=valeur*(16**(2-(compteur+1)))
    compteur+=1

print ("La valeur decimale est: ", decimal)


    

#b8
#10111000
#04
#00000100
#de
#11011110
#f7
#11110111

#4158522552

