#!/usr/bin/env python
#coding: utf-8
import os, platform

validos = []
invalidos = []


#ping
def ping(ip):

    if platform.system().lower() == "windows":
        ping_str = "-n 1"
    else:
        ping_str = "-c 1"

    resposta = os.system("ping " + ping_str + " " + ip)
    return resposta == 0


#abrindo ip
with open('ips.txt', 'r') as f:
    content = f.readlines()

#lendo cada ip que vem do txt
for each in content:
    each = each.replace('\n', '')
    print(each)
    if (ping(each)):
        validos.append(each)
    else:
        invalidos.append(each)

#printando output
with open('output.txt', 'w') as f:
    f.write("[Endereços Válidos]\n")
    for element in validos:
        f.write(element)
        f.write("\n")
    f.write("\n[Endereços Inválidos]\n")
    for element in invalidos:
        f.write(element)
        f.write("\n")

print("\n[Endereços Válidos]")
for element in validos:
    print(element)

print("\n[Endereços Inválidos]")
for element in invalidos:
    print(element)
