#!/usr/bin/env python
# coding: utf-8
# loja de tintas
import math

#input de dados
tamanho = input("Qual o tamanho em metros quadrados da área pintada? ")
litrosEmLata = input("Quantos litros têm uma lata? ")
custoDeUmaLata = input("Qual o custo de uma lata? ")
metrosPorLitro = input("A tinta consegue cobrir quanto metros por litro? ")

#processamento
quantosLitros = tamanho / metrosPorLitro
quantasLatas = math.ceil(float(quantosLitros) / float(litrosEmLata))
custoDaTinta = quantasLatas * custoDeUmaLata

#output
quantidade = "A quantidade total de latas será {} latas"
custo = "O custo total das tintas será de {} reais"
print(quantidade.format(quantasLatas))
print(custo.format(custoDaTinta))
