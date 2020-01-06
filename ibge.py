#!/usr/bin/env python
#coding: utf-8

import csv

with open('RedeUrbana.csv', 'r') as dados:
    with open('saida.txt','w') as saida:
        reader = csv.reader(dados)
        next(reader, None)
        for registro in reader:
            saida.write(f'{registro[3]}, {registro[4]}, {registro[5]}, {registro[7]}\n')

