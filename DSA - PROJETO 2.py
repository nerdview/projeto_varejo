#!/usr/bin/env python
# coding: utf-8

# # <font color='black'>Data Science Academy</font>
# 
# ## <font color='black'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>
# 
# ## <font color='red'>Análise Exploratória de Dados em Linguagem Python Para a Área de Varejo</font>

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# In[2]:


# Importar as bibliotecas necessárias
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sea 
import datetime as dt


# In[3]:


# Importar a função DataFrame do Pandas
from pandas import DataFrame


# In[4]:


# Carregar os dados para analise:
varejo =pd.read_csv(r"C:\Users\Lukas\Documents\Data Science\DSA\Cap13\dados\dataset.csv")


# In[5]:


# Verificar se os dados foram carregados corretamente 
varejo.head()


# ## Análise Exploratória 

# In[6]:


# Verificando os conjuntos de dados:
varejo.columns


# In[8]:


# Verificando o tipo de dado de cada coluna
varejo.dtypes


# In[10]:


# Valores estatísticos iniciais observados para vendas: 
varejo['Valor_Venda'].describe()


# In[11]:


# Verificando se há registros duplicados: 
varejo[varejo.duplicated()]


# In[12]:


# Verificando de há valores ausentes
varejo.isnull().sum()


# ## Business IIntelligence - Perguntas de negócio: 

# ### 1 - Qual cidade com maior valor de venda de produtos da categoria 'Office Supplies'?

# In[13]:


# Imprimindo os dados da categoria:  
varejo[ ['Cidade', 'Categoria'] ]


# In[32]:


# Filtrando pelo índice
filtro = varejo['Categoria'] == 'Office Supplies'
resultado = varejo[filtro]
resultado.head()


# In[26]:


# Agrupar por cidade e calcular a soma das vendas
cidade = resultado.groupby('Cidade')['Valor_Venda'].sum()

# Encontrar a cidade com a maior soma de vendas
cidade_maior = cidade.idxmax()
vendas = cidade.max()

# Resultado: 
print(f"A cidade com maior valor de venda de produtos é {cidade_maior} com um total de vendas de {vendas}.")


# ## Pergunta de Negócio 2:
# 
# ### Qual o Total de Vendas Por Data do Pedido?
# 
# Demonstre o resultado através de um gráfico de barras.

# In[52]:


# Converter as datas para Datetime: 
varejo['Data_Pedido'] = pd.to_datetime(varejo['Data_Pedido'], format='%d/%m/%Y')

# Total de vendas e datas: 
data_do_pedido = varejo.groupby(varejo['Data_Pedido'].dt.to_period("M"))['Valor_Venda'].sum()

#Criando o gráfico: 
plt.figure(figsize=(12, 6))
ax = data_do_pedido.plot(kind='bar', color='green', edgecolor='black')

# Ajustar os rótulos no eixo x
intervalo = 3  # Exibir a cada 3 meses
ax.set_xticks(range(0, len(data_do_pedido), intervalo))
ax.set_xticklabels([str(periodo) for periodo in data_do_pedido.index[::intervalo]], rotation=45, ha="right")

# Plotar o label 
plt.title('Total de Vendas por Data')
plt.xlabel('Data')
plt.ylabel('Total de Vendas')
plt.show()


# ## Pergunta de Negócio 3:
# 
# ### Qual o Total de Vendas por Estado?
# 
# Demonstre o resultado através de um gráfico de barras.

# In[62]:


# Agrupar por estado e calcular o total das vendas
vendas_por_estado = varejo.groupby('Estado')['Valor_Venda'].sum()

# Plotar o gráfico de barras
plt.figure(figsize=(12, 5))
vendas_por_estado.plot(kind='bar', color='green', edgecolor='black')
plt.title('Total de Vendas por Estado')
plt.xlabel('Estado')
plt.ylabel('Total de Vendas')
plt.show()


# ## Pergunta de Negócio 4:
# 
# ### Quais São as 10 Cidades com Maior Total de Vendas?
# 
# Demonstre o resultado através de um gráfico de barras.

# In[87]:


# Agrupar por estado e cidade e calcular o maior total das vendas: 
vendas_por_cidade = varejo.groupby('Cidade')['Valor_Venda'].sum()

# Ordenar as cidades pelo total de vendas em ordem decrescente
cidades_ordenadas = vendas_por_cidade.sort_values(ascending=False)

# Selecionar as top 10 cidades com os maiores valores de venda
top_10_cidades = cidades_ordenadas.head(10)

# Plotar o gráfico de barras
top_10_cidades.plot(kind='bar', color='green', edgecolor='black')
plt.title('Total de Vendas por Estado')
plt.xlabel('Estado')
plt.ylabel('Total de Vendas')
plt.show()


# ## Pergunta de Negócio 5:
# 
# ### Qual Segmento Teve o Maior Total de Vendas?
# 
# Demonstre o resultado através de um gráfico de pizza.

# In[97]:


# Segmento com maior total de vendas:
segmento = varejo.groupby('Segmento')['Valor_Venda'].sum()

# Ordenar o segmento por número de vendas:
melhor_segmento = segmento.sort_values(ascending=False)

top_segmento = melhor_segmento.nlargest(3)

# Plot gráfico de pizza:
plt.pie(top_segmento, labels=top_segmento.index, startangle = 90, shadow = False)
plt.show()


# In[95]:


melhor_segmento.head()


# ## Pergunta de Negócio 6 (Desafio Nível Baby):
# 
# ### Qual o Total de Vendas Por Segmento e Por Ano?

# In[99]:


# Verificando o formato das datas: 
varejo['Data_Pedido'].head()


# In[103]:


# Converter a coluna 'Data' para o formato datetime
varejo['Data_Pedido'] = pd.to_datetime(varejo['Data_Pedido'])

# Criar colunas 'Ano' e 'Mes' a partir da coluna 'Data'
varejo['Ano'] = varejo['Data_Pedido'].dt.year
varejo['Mes'] = varejo['Data_Pedido'].dt.month

# Agrupar por segmento, ano e calcular o total das vendas
total_vendas_ano = varejo.groupby(['Segmento', 'Ano'])['Valor_Venda'].sum().reset_index()


# In[107]:


# Visualiza o total de vendas: 
total_vendas_ano


# ## Pergunta de Negócio 7 (Desafio Nível Júnior):
# 
# Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:
# 
# - Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
# - Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
# 
# ### Quantas Vendas Receberiam 15% de Desconto?

# In[110]:


# Primeiro precisamos classifocar o total de vendas acima de 1000: 
varejo[varejo['Valor_Venda'] > 1000]


# In[115]:


# Agora classificaremos os pedidos com desconto em uma nova coluna: 
varejo['Desconto'] = varejo['Valor_Venda'].apply(lambda x: 0.15 if x > 1000 else 0.10)

# Contar quantas vendas receberiam 15% de desconto
vendas_com_desconto = varejo[varejo['Desconto'] == 0.15].shape[0]

# Visualizar o total de vendas com desconto: 
print(f'Total de vendas com desconto: {vendas_com_desconto}')


# In[117]:


# Verificar se a coluna criada está mostrando o desconto
varejo.head()


# ## Pergunta de Negócio 8 (Desafio Nível Master):
# 
# ### Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior. Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?

# In[120]:


# Primeiro faremos a media do valor de venda sem desconto: 
varejo['Valor_Venda'].mean()

