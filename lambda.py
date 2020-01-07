#!/usr/bin/env python
#coding: utf-8

compras = (
    {'quantidade': 2 , 'preço': 200},
    {'quantidade': 7 , 'preço': 100},
    )


totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preço'],compras
    )
)
quantidade = tuple(
    map(
        lambda compra: compra['quantidade'], compras
    )
)

print('quantidade: ', sum(quantidade))
print('Preços totais: ', list(totais))
print('total: ', sum(totais))