import pandas as pd
import pandera as pa

valores_ausentes = ['**', '###!', '####', '****', '*****', 'NULL']
df = pd.read_csv("ocorrencia_2010_2020.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True, na_values=valores_ausentes)
df.drop(df.columns[[1, 3, 4, 6, 7, 10, 14, 15, 16, 17, 18, 20, 21]], axis=1, inplace=True)
pd.set_option('display.max_columns', 10)
df.head(10)
schema = pa.DataFrameSchema(
    columns={
        "codigo_ocorrencia": pa.Column(pa.Int, required=False),
        "codigo_ocorrencia2": pa.Column(pa.Int),
        "ocorrencia_classifcacao": pa.Column(pa.String),
        "ocorrencia_cidade": pa.Column(pa.String),
        "ocorrencia_uf": pa.Column(pa.String, pa.Check.str_length(2, 2), nullable=True),
        "ocorrencia_aerodromo": pa.Column(pa.String, nullable=True),
        "ocorrencia_dia": pa.Column(pa.DateTime),
        "ocorrencia_hora": pa.Column(pa.String, pa.Check.str_matches
        (r'^([0-1]?[0-9]│[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'), nullable=True), "total_recomendacoes":pa.Column(pa.Int)
    }
)
#comandos de busca
df.dtypes
df.loc[1]
df.iloc[-1]
df.iloc[10:15]
df['ocorrencia_uf']

#comandos para manipulação de valores nulos
df.isna(). sum()
df.isnull().sum()
df.ocorrencia_uf.isnull()
filtro = df.ocorrencia_uf.isnull()
df.loc[filtro]
df.isna().sum()
df.count() #não conta valor nulo

#comandos para fazer busca de dado específico com uso de filtro
filtro1 = df.total_recomendacoes > 10
df.loc[filtro1, ['ocorrencia_cidade', 'total_recomendacoes']]
filtro2 = df.ocorrencia_uf == 'SP'
df.loc[filtro2]
df.loc[filtro1 & filtro2]
filtro3 = df.ocorrencia_classificacao.isin(['INCIDENTE GRAVE', 'INCIDENTE'])
df.loc[filtro2 & filtro3]

#comandos para buscar com filtro arrays
filtro4 = df.ocorrencia_cidade.str[0] == 'C'
filtro5 = df.ocorrencia_cidade.str[-2:] == 'MA'
filtro6 = df.ocorrencia_cidade.str.contains == 'CO'
filtro7 = df.ocorrencia_cidade.str.contains == ('MA|AL')

#comandos para buscar com filtro por data e hora
filtro_ano = df.ocorrencia_dia.dt.year == 2015
filtro_mes = df.ocorrencia_dia.dt.month == 12
filtro_dia = df.ocorrencia_dia.dt.day == 8
df.loc[filtro_ano & filtro_mes]
df['ocorrencia_dia_hora'] = pd.to_datetime(df.ocorrencia_dia.astype(str)+' ' + df.ocorrencia_hora)
filtro_ini = df.ocorrencia_dia_hora >= '2015-12-03 11:00:00'
filtro_fim = df.ocorrencia_dia_hora <= '2015-12-08 14:3 0:00'
df.loc[filtro_ini & filtro_fim]

#comandos para agrupamento de dados para tornar busca mais especifica e eficiente
filtro1 = df.ocorrencia_dia.dt.year == 2010
filtro2 = df.ocorrencia_dia.dt.month == 3
df_2015_03 = df.loc[filtro1 & filtro2]
df_2015_03.groupby(['ocorrencia_classificacao']).size().sort_values()
filtro3 = df.ocorrencia_uf.isin(['SP', 'MG', 'ES', 'RJ'])
df_sudeste_2010 = df.loc[filtro3 & filtro1]
df_sudeste_2010.groupby(['ocorrencia_classificacao','ocorrencia_uf']).size()
df_sudeste_2010.groupby(['ocorrencia_cidade']).size().sort_values()
filtro4 = df_sudeste_2010.ocorrencia_cidade == 'RIO DE JANEIRO'
df_sudeste_2010.loc[filtro4].total_recomendacoes.sum()
filtro5 = df_sudeste_2010.total_recomendacoes > 0
df_sudeste_2010.loc[filtro5].groupby(['ocorrencia_cidade']).total_recomendacoes.sum().sort_values()
print(df_sudeste_2010.loc[filtro5].groupby(['ocorrencia_cidade', df_sudeste_2010.ocorrencia_dia.dt.month]).total_recomendacoes.sum())


