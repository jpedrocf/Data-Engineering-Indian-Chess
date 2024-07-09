# Databricks notebook source
# MAGIC %md
# MAGIC # **Projeto de MVP**
# MAGIC
# MAGIC ## O objetivo desse MVP é checar a evolução da Índia no xadrez.
# MAGIC ## 
# MAGIC ## As perguntas que quero responder são:
# MAGIC
# MAGIC
# MAGIC - A Índia é uma potência no xadrez?
# MAGIC - Existe evolução no xadrez indiano?
# MAGIC - Quais são as aberturas que mais têm sucesso no xadrez indiano comparadas ao resto do mundo?
# MAGIC
# MAGIC Para responder a essas perguntas, reuni dados do site da FIDE, que é a Federação Internacional de Xadrez, e do jornal diário de xadrez chamado "The Week in Chess".
# MAGIC
# MAGIC Na plataforma da FIDE, baixei 113 arquivos referentes ao período de fevereiro de 2015 até junho de 2024. Estes arquivos estão relacionados a dados de jogadores de xadrez. Entre esses dados estão o ID pessoal de cada jogador (FIDE ID), o nome do jogador, a nacionalidade, o sexo, títulos conquistados, ratings, ano de nascimento e uma flag que indica se o jogador está ativo ou inativo. Os arquivos, quando baixados, vinham com um nome padrão, onde do índice 9 ao 14 continha o mês e o ano referente à tabela. Todos os arquivos eram XML. Para otimizar, criei um conversor de XML para Parquet, que lia todos os arquivos salvos na pasta e convertia para Parquet em uma única tabela, esse mesmo código também criava 2 novas colunas, uma contendo o nome do próprio arquivo e outra contendo a data de download.
# MAGIC
# MAGIC Já a plataforma "The Week in Chess" me forneceu dados de campeonatos recentes jogados pelos melhores jogadores do mundo, contendo informações como nome e local do campeonato, data, round, jogador de brancas, jogador de negras, resultado, título do jogador de brancas, título do jogador de negras, ranking do jogador de brancas, ranking do jogador de negras, abertura jogada, FIDE ID de cada jogador e a data do evento.
# MAGIC
# MAGIC Esses dados foram processados por um código Python, que agregou todos os arquivos em uma única tabela. Também adicionei um identificador único para cada partida.
# MAGIC
# MAGIC Após a junção dos arquivos de partidas e de jogadores, realizei o upload das tabelas no Databricks e as coloquei em databases que criei internamente. Os bancos de dados que criei foram o Bronze, Prata e Ouro, para utilizar a arquitetura de dados em camadas (medalhão).
# MAGIC
# MAGIC Tanto as partidas quanto os jogadores foram colocados no banco de dados Bronze para passarem pelo processo de ETL.
# MAGIC
# MAGIC Neste momento, utilizei o notebook do Databricks para realizar conferências e fazer limpezas, deixando o passo a passo descrito em cada um deles.
# MAGIC
# MAGIC Depois de realizar o processo de ETL, salvei o DataFrame criado no database Silver, onde fiz uma limpeza mais criteriosa de colunas, filtragem de dados e junção de tabelas, para salvar no database Gold.
# MAGIC
# MAGIC Com as tabelas criadas no database Gold, montei um dashboard de apresentação para responder às perguntas feitas no início deste MVP.
# MAGIC
