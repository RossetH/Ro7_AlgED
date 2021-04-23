import pandas as pd  # importação/exportação de dados
import numpy as np   #  manipulação de vetor e matriz

path = "pandas_class/datasets/"

#criar dataframe no form/ato de dicionário
df1 = pd.DataFrame({
    "Matricula": [1, 2, 3, 4,  5,  6,  7,  8,  9,  10,  11,  12,  13,  14,  15,  16, 17,  18,  19,  20],
    "Curso":     ["Mat","Est","CC","CC","Mat","Eng","Est","Eng","Fis","Mat","CC","CC","Est","Eng","Mat","CC","Eng","Est","Mat","Est"],
    "Prova1":    [9.91,	7.95,	7.34,	9.11,	1.05,	0.66,	2.29,	0.28,	2.82,	2.28,	1.15,	4.2,	0.79,	9.34,	2.13,	8.3,	6.06,	4.51,	4.23,	8.43],
    "Prova2":    [8.82,	5.65,	1.77,	8.91,	7.44,	0.62,	0.84,	5.33,	6.94,	2.76,	2.83,	7.42,	1.55,	6.73,	3.31,	4.8,	8.27,	0.61,	5.55,	7.3],
    "Faltas":    [4, 1, 2, 0, 1, 4, 3, 4, 2, 3, 3, 4, 1, 3, 2, 0, 2, 2, 0, 1]})

df2 = pd.DataFrame({
    "Matricula": [21,	22,	23,	24,	25,	26,	27,	28,	29,	20,	31,	32,	33,	34,	35,	36,	37,	38,	39,	40],
    "Curso":	   ["CC",	"Mat",	"Eng",	"Eng",	"Mat", "Fis",	"Mat",	"Eng",	"Fis",	"CC",	"Eng",	"Eng",	"Est",	"Fis", "Mat",	"Eng",	"Eng",	"Est",	"CC",	"Mat"],
    "Prova1":	   [5.35,	2.39,	8.17,	7.79,	8.02,	3.83,	8.48,	2.55,	7.64,	6.72,	1.00,	6.19,	1.15,	9.43,	8.73,	8.99,	0.83,	4.12,	2.07,	0.16],
    "Prova2":	   [2.94,	8.47,	4.71,	8.18,	9.92,	4.28,	5.22,	9.83,	2.14,	9.46,	1.14,	3.79,	0.39,	5.72,	6.56,	5.27,	1.43,	8.70,	2.70,	1.37],
    "Faltas":    [3, 3, 2, 1, 3, 1, 2, 4, 4, 4, 4, 3, 1, 0, 2, 2, 1, 0, 2, 4]})

print(df1, df2)

# criar dataframe a partir de um arquivo CSV
file = path + 'notas1.csv'
df1 = pd.read_csv(file)
print(df1)

file = path + 'notas2.csv'
df2 = pd.read_csv(file)
print(df2)

# criar dataframe a partir de um arquivo TXT

file = path + 'notas1.txt'
df1 = pd.read_table(filepath_or_buffer = file,sep = "\t", comment = "#")
print(df1)

file = path + 'notas2.txt'
df2 = pd.read_table(filepath_or_buffer = file,sep = "\t", comment = "#")
print(df2)

# Ordenar dataframes

#df1.sort_values(by = "Matricula", ascending=True)
df1.sort_values(by = "Prova1", ascending=True)

# Listar informações
print("Dimensão ", df1.shape)
print("id linnhas ", df1.index)
print("id colunas ", df1.columns)
print("Descrição ", df1.info())

# Seleção de elementos pelo  nome das COLUNAS
cols = ["Matricula", "Prova2"]
print(df1["Curso"])
print(df1[ ["Curso", "Prova1"] ]) ## cuidar colchetes duplo
df2 = df1[cols]

# fatiando elementos (LOC) -- LINHAS(s), intervalo de linhas
df1.loc[1]
df1.loc[[1,2,3]]
df1.loc[1:5]

# fatiando elementos (LOC) -- linha(s) e colunas
df1.loc[[1,2],["Matricula", "Prova1"]]
df1.loc[  :   ,["Matricula", "Prova1"]]
df1.loc[[1,2], :]

# fatiando elementos (ILOC) -- linha(s), colunas, intervalo de linhas
df1.iloc[:, 2:4] 
df1.iloc[:, -3:]
df1.iloc[:, [1, 3]]
df1.iloc[:, range(0, 3)]
df1.iloc[:3, range(0, 3)]
df1.iloc[3:8, range(0, 3)]

# selecionar posições pares (linhas e colunas)
x = df1.shape
indexLin = np.arange(0, x[0])
indexCol = np.arange(0, x[1])
setLin = [indexLin[i] for i in range(0, x[0], 2)]
setCol = [indexCol[i] for i in range(0, x[1], 2)]

df1.iloc[setLin, setCol]
df1.iloc[setLin, :]
df1.iloc[:, setCol]

# selecionar intervalo 3-5 5-8
df1.iloc[3:5]
df1.iloc[5:8]

# selecinar todas exceto lista (ILOC)
import numpy as np
x = df1.shape
indexCol = np.arange(0, x[1])
tabuList = [1,2]
setCol = [indexCol[i] for i in indexCol if not i in tabuList]

df1.iloc[:, setCol]

# selecinar todas exceto lista (LOC)
import numpy as np

nameTabu = ["Curso", "Prova1"]
df1.loc[:, ~df1.columns.isin(nameTabu)]

# Apenas as de tipo numérico 
type(df1.dtypes)
sel1 = df1.dtypes == "int64"
sel2 = df1.dtypes == "float64"
df1.loc[:, sel2]

# Seleção de variáveis por padrão de caracteres (regex).
df = df1.filter(regex = "^Prova") # Começa com "Prova".
print(df)

# Seleção de variáveis por padrão de caracteres (regex).
df = df1.filter(regex = "\d$")    # Termina com número.
print(df)

# Selecionar colunas sem NaNs
import numpy as np

df1 = pd.DataFrame({
    "Matricula": [1, 2, 3, 4,  5,  6,  7,  8,  9,  10,  11,  12,  13,  14,  15,  16, 17,  18,  19,  20],
    "Curso":     ["Mat","Est","CC","CC","Mat","Eng","Est","Eng","Fis","Mat","CC","CC","Est","Eng","Mat","CC","Eng","Est","Mat","Est"],
    "Prova1":    [9.91,	7.95,	7.34,	9.11,	1.05,	0.66,	2.29,	0.28,	2.82,	2.28,	1.15,	4.2,	0.79,	9.34,	2.13,	8.3,	6.06,	4.51,	4.23,	8.43],
    "Prova2":    [8.82,	5.65,	1.77,	8.91,	7.44,	0.62,	0.84,	5.33,	6.94,	2.76,	2.83,	7.42,	1.55,	6.73,	3.31,	4.8,	8.27,	0.61,	5.55,	7.3],
    "Faltas":    [4, 1, 2, 0, 1, 4, 3, 4, 2, 3, 3, 4, 1, 3, 2, 0, 2, 2, 0, 1]})

df1.loc[ len(df1)  ] = [21, "Est", np.NaN, np.NaN, np.NaN]
df1.loc[ len(df1) ] = [22, "Fis", np.NaN, np.NaN, np.NaN]
df1

df2 = df1.loc[:, df1.notnull().all()]
df2

#selecionar uma coluna baseada em outra
df1 = pd.DataFrame({
    "Matricula": [1, 2, 3, 4,  5,  6,  7,  8,  9,  10,  11,  12,  13,  14,  15,  16, 17,  18,  19,  20],
    "Curso":     ["Mat","Est","CC","CC","Mat","Eng","Est","Eng","Fis","Mat","CC","CC","Est","Eng","Mat","CC","Eng","Est","Mat","Est"],
    "Prova1":    [9.91,	7.95,	7.34,	9.11,	1.05,	0.66,	2.29,	0.28,	2.82,	2.28,	1.15,	4.2,	0.79,	9.34,	2.13,	8.3,	6.06,	4.51,	4.23,	8.43],
    "Prova2":    [8.82,	5.65,	1.77,	8.91,	7.44,	0.62,	0.84,	5.33,	6.94,	2.76,	2.83,	7.42,	1.55,	6.73,	3.31,	4.8,	8.27,	0.61,	5.55,	7.3],
    "Faltas":    [4, 1, 2, 0, 1, 4, 3, 4, 2, 3, 3, 4, 1, 3, 2, 0, 2, 2, 0, 1]})

#df1[df1.Prova1 > df1.Prova2]

#df1.Curso[df1.Prova1 > 7]

df1.Faltas[(df1.Prova1+df1.Prova2)/2 > 5]