#!/usr/bin/env python
#coding: utf-8

salarioPorHora = input("Quanto você ganha por hora?  ")
horasTrabalhadas = input("Quantas horas você trabalha por mês?  ")

print(salarioPorHora)
print(horasTrabalhadas)
salarioBruto = int(salarioPorHora) * int(horasTrabalhadas)

emIR = salarioBruto * 0.11
emINSS = salarioBruto * 0.08
emSindicato = salarioBruto * 0.05

salarioLiquido = salarioBruto - emIR - emINSS - emSindicato

txtBruto = "Salário Bruto: R${}"
print(txtBruto.format(salarioBruto))

txtIR = "IR (11%): R$ {}"
print(txtIR.format(emIR))

txtINSS = "INSS (8%): R$ {}"
print(txtINSS.format(emINSS))

txtSindicato = "Sindicato (5%): R$ {}"
print(txtSindicato.format(emSindicato))

liquido = "Salário Líquido: R$ {}"
print(liquido.format(salarioLiquido))