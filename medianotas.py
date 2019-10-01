#!/usr/bin/env python
#coding: utf-8

ee1 = input("Qual a nota da sua primeira prova? ")
ee2 = input("Qual a nota da sua segunda prova? ")

media = float(ee1 + ee2) / float(2)
if (media < 7):
    print("Você não foi aprovado. Precisará fazer final e tirar {}".format(
        10 - media))
    final = input("Qual a nota da final? ")

    mediafinal = float(media + final) / 2
    if (mediafinal < 5):
        print("Você foi reprovado mesmo!")
    else:
        print("Voce foi aprovado com média final {}".format(mediafinal))
else:
    print("Você foi aprovado com média {}".format(media))
