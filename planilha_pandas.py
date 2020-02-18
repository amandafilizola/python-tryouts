import pandas as pd

x = pd.read_excel(r"./planilha.ods")

print(x['Idade'][3])

