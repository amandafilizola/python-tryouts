import matplotlib.pyplot as plt

dados = open('populacao-brasileira.csv').readlines()

x = []
y = []

for i in range(len(dados)):
  if i != 0:
    linha  = dados[i].split(";")
    x.append(int(linha[0]))
    y.append(int(linha[1]))

anomin = min(x)
anomax = max(x)

plt.bar(x,y)
plt.title('Crescimento da populaão brasileira '+ str(anomin) + '-' + str(anomax))
plt.xlabel('Ano')
plt.ylabel('População em milhões')
plt.show()