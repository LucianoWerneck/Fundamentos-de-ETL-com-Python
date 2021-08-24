#Extração e Validando de Dados e aprendendo dataframe
import pandas as pd
import pandera as pa

#comando para extração organização dos dados
df = pd.read_csv("ocorrencia_2010_2020.csv", sep=";", parse_dates=["ocorrencia_dia"], dayfirst=True)
#comando para deletar colunas
del df["codigo_ocorrencia1"]
df = df.drop(df.columns[[ 2, 3, 5, 6, 9, 13, 14, 15, 16, 17, 19, 20]], axis=1)

#comando para realizar exibição 10 colunas do dataframe
pd.set_option('display.max_columns', 10)

#comando para realizar exibição 10 linhas
print(df.tail(10))


#comando lista as informações do arquivo
print(df.info)

#comando que mostra os tipos de dados das colunas
print(df.dtypes)

#comando para acessar a coluna, expecificando a busca por mês após ter
#sido converter o tipo de obejeto para datetime
print(df.ocorrencia_dia.dt.month)

#comando de validação de cada dado recebido pelo dataframe
schema = pa.DataFrameSchema(
    columns = {
        "codigo_ocorrencia":pa.Column(pa.Int, required=False),
        "codigo_ocorrencia2":pa.Column(pa.Int),
        "ocorrencia_classifcacao":pa.Column(pa.String),
        "ocorrencia_cidade":pa.Column(pa.String),
        "ocorrencia_uf":pa.Column(pa.String, pa.Check.str_length(2,2)),
        "ocorrencia_aerodromo":pa.Column(pa.String),
        "ocorrencia_dia":pa.Column(pa.DateTime),
        "ocorrencia_hora":pa.Column(pa.String, pa.Check.str_matches
        (r'^([0-1]?[0-9]│[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'), nullable=True),
        "total_recomendacoes":pa.Column(pa.Int)
    }
)


