# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual /
# de representação que cada estado teve dentro do valor total mensal da distribuidora.
import pandas as pd 


data = {
    'Estado': ['SP', 'RJ', 'MG', 'ES','Outros'],
    'valor' : [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
}

df = pd.DataFrame(data)

valor_total = df['valor'].sum()

df['percentual(%)'] = (df['valor'] / valor_total) * 100

print(df)
