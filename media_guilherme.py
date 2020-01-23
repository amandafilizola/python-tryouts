#!/usr/bin/env python
#coding: utf-8

#1° trim
prova1 = float(input("Qual a sua nota da AV1 do 1° trim?"))
prova2 = float(input("Qual a sua nota da AV2 do 1° trim?"))

trim1 = [prova1, prova2]

maxtrim1 = max(trim1)

media1 = float(prova1+prova2)/2
print(media1)
if(media1>7):
  print("PARABÉNS, VOCÊ PASSOU!!!              no 1° trim...")
else:
  rec1 = float(input("Qual a sua nota da recuperação do 1° trim?"))

  media1 = float(rec1+maxtrim1)/2
  if(media1>7):
    print("PARABÉNS, VOCÊ PASSOU!!!              no 1° trim...")
  else:
    print("Ainda dá tempo")


#2° trim
prova3 = float(input("Qual a sua nota da AV1 do 2° trim?"))
prova4 = float(input("Qual a sua nota da AV2 do 2° trim?"))

trim2 = [prova3, prova4]

maxtrim2 = max(trim2)

media2 = float(prova3+prova4)/2
if(media2>7):
  print("PARABÉNS, VOCÊ PASSOU!!!              no 2° trim...")
else:
  rec2 = float(input("Qual a sua nota da recuperação do 2° trim?"))

  media2 = float(rec2+maxtrim2)/2
  if(media2>7):
    print("PARABÉNS, VOCÊ PASSOU!!!              no 2° trim...")
  else:
    print("Talvez ainda dê tempo")


#3° trim
prova5 = float(input("Qual a sua nota da AV1 do 3° trim?"))
prova6 = float(input("Qual a sua nota da AV2 do 3° trim?"))

trim3 = [prova6, prova5]

maxtrim3 = max(trim3)

media3 = float(prova5+prova6)/2
if(media3>7):
  print("PARABÉNS, VOCÊ PASSOU!!!              se você não tiver ficado em nos outros trim")
else:
  rec3 = float(input("Qual a sua nota da recuperação do 3° trim?"))

  media3 = float(rec3+maxtrim3)/2
  if(media3>7):
    print("PARABÉNS, VOCÊ PASSOU!!!              se você não tiver ficado em nos outros trim")
  else:
    print("não sei se ainda dá tempo")


mediafin = (media1+media2+media3)/3

if(mediafin>7):
  print("AGORA VOCÊ PASSOU COM CERTEZA!!!")
else:
  recfin = float(input("Qual a sua nota da recuperação final?"))
  if(10-mediafin<recfin):
    print("AEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
  else:
    print("SUCESSO                 ao contrário")