# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
import json
import pandas as pd


with open('dados.json', 'r') as file:
    dados = json.load(file)

df = pd.json_normalize(dados)

faturamento_maximo_dia = df['valor'].max()
faturamento_minimo_dia = df['valor'].min()

# tratando data frame para que os dias sem faturamento não entre no cálculo da média
df_filtrado = df[df['valor'] != 0]

faturamento_medio_mensal = df_filtrado['valor'].mean()

print(f'Faturamento máximo em um dia: {faturamento_maximo_dia}')
print(30 * '-')

print(f'Faturamento mínimo em um dia: {faturamento_minimo_dia}')
print(30 * '-')

print(f'Faturamento média mensal: {faturamento_medio_mensal}')
print(30 * '-')
