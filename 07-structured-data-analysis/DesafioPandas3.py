
# coding: utf-8

# ## Alterando o dataset original

# In[96]:


# Primeiro vamos copiar o dataset original para outra variável, para não dar xabu no resto da aula :P


# In[97]:


# Agora vamos ver os valores da coluna LearningDataScience


# In[46]:


def replace_value(row):
    if row == "Yes, I'm focused on learning mostly data science skills":
        return "yes"
    elif row == "Yes, but data science is a small part of what I'm focused on learning":
        return "so so"
    elif row == "No, I am not focused on learning data science skills":
        return "no"


# In[98]:


# Agora vamos aplicar a função replace_value a todas as linhas do LearningDataScience. 
# Crie uma nova coluna chamada LearningDataScienceSimple


# Agora podemos ver os novos valores desses campos

# In[99]:


# Agora vamos ver os valores da coluna LearningDataScienceSimple


# In[49]:


# Qual o shape do dataset atual?


# E agora que a outra coluna muito complexa não serve mais, podemos descartá-la

# In[50]:


# Descarte a coluna LearningDataScience


# In[100]:


# Qual o shape do dataset atual?


# Pela quantidade de linhas no dataset percebemos que o `value_counts()` não retorna os valores nulos - e nós temos MUITOS valores nulos nessa coluna. Podemos utilizar um método do pandas para trocar os NAs por uma categoria nossa.

# In[101]:


# Substitua os nulos pela frase "did not answer the question"


# In[102]:


# Agora vamos ver os valores da coluna LearningDataScienceSimple


# Outra forma de alterar o dataset é utilizando funções _in place_. Para isso utilizaremos o `lambda`

# Por exemplo: E se eu quiser atualizar a idade dos participantes? O dataset foi coletado em 2017 e já estamos em 2018

# In[103]:


# Ao invés de usar uma função que soma +1, vamos escrever a nossa com o lambda


# Vamos ver se funcionou? Vamos dar uma olhada nos primeiros 5 registros, com a coluna 'Age' e a 'NewAge' lado a lado

# Ficou mais claro a proporção de pessoas que não responderam agora o/

# ### Desafio 3 - Para casa

# Separar os datasets pelas pessoas que os responderam. Para isso você vai ter que carregar o dataset `schema.csv`.
# 
# O dataset `schema.csv` possui a coluna `Asked` - lá você conseguirá ver quais tipos de pessoas responderam as perguntas - E então agrupe as perguntas pela pessoas que as responderam. 
# 
# Como uns datasets ficariam muito pequenos, sugiro que você utilize os seus conhecimentos recém adquiridos e crie 4 datasets distintos. Além de criá-los você deve salvá-los como `.csv`. Vamos usar esses datasets na próxima aula.

# ![panda_playground](https://media.giphy.com/media/ieaUdBJJC19uw/giphy.gif)
