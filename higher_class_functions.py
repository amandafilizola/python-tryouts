#!/usr/bin/env python
#coding: utf-8

from first_class_functions import dobro, quadrado

def process(titulo, lista, funcao):
    print(f'Processando: { titulo }')
    for i in lista:
        print(f'o { titulo } de ',i,' = ',funcao(i))

if __name__ == "__main__":
    process('Dobro', range(1,10), dobro)
    process('Quadrado', range(1,10), quadrado)

