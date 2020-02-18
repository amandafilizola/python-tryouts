# visualização de dados em python

import matplotlib.pyplot as plt

#dados
x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 4, 6]
z = [200, 500, 100, 330, 100]

#constantes
titulo = "Scatterplot"
eixox = "Eixo X"
eixoy = "Eixo Y"

# titulo
plt.title(titulo)

# eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x1, y1, label="Os Pontos", color="r", marker=".", s=z)
plt.plot(x1,y1, linestyle=":",color="k")
plt.legend()

# plt.show()
plt.savefig("figura1.png", dpi=300)
