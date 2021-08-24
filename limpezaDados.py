import pandas as pd


df = pd.read_csv("ocorrencia_2010_2020.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True)
del df["codigo_ocorrencia1"]
df = df.drop(df.columns[[ 2, 3, 5, 6, 9, 13, 14, 15, 16, 17, 19, 20]], axis=1)
df.head(5)

#comando para acessar dados utilizando o rotulo da linha
print(df.loc[1, 'ocorrencia_cidade'])
print(df.loc[1:3])
print(df.loc[[10, 40]])
print(df.loc[:, 'ocorrencia_cidade'])

#Manipulando o indece do dataframe
print(df.codigo_ocorrencia.is_unique)
print(df.set_index('codigo_ocorrencia', inplace=True))
print(df.loc[40324])
df.reset_index(drop=True, inplace=True)
print(df.head())

#comando para alteração dos dados do dataframe
print(df.head(1))
df.loc[0, 'ocorrencia_hora'] = ''
print(df.head(1))
df.loc[:,'total_recomendacoes'] = 10
df['ocorrencia_uf_bkp'] = df.ocorrencia_uf
print(df.head(2))

#comando para alterar os dados de uma coluna com base nos dados de outra coluna
df.loc[df.ocorrencia_uf == 'SP', ['ocorrencia_classificacao']] = 'GRAVE'

#comando para fazer limpeza dos dados
df.loc[df.ocorrencia_aerodromo == '****', ['ocorrencia_aerodromo']] = pd.NA
df.replace(['**', '###', '####', '****', '*****', 'NULL'], pd.NA, inplace=True)
pd.set_option('display.max_columns', 10)
df.head()
df.isna().sum()

#comando para colocar um valor num campo de dado não informado
df.fillna(0, inplace=True)
df.fillna(value={'total_recomendacoes':10})