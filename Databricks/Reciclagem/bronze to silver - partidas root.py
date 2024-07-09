# Databricks notebook source
# MAGIC %sql
# MAGIC select *
# MAGIC from bronze.partidas_campeonato

# COMMAND ----------

partidas_df1 = spark.table('bronze.partidas_campeonato')

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.functions import col
import datetime

# COMMAND ----------

partidas_df1.printSchema()

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT white, white_fide_id
# MAGIC FROM bronze.partidas_campeonato
# MAGIC WHERE white = 'Selley,Susan A'

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, LongType, DoubleType, DateType

schema = StructType([
    StructField("id", LongType(), False),
    StructField("event", StringType(), True),
    StructField("site", StringType(), True),
    StructField("date", DateType(), True),
    StructField("round", DoubleType(), True),
    StructField("white", StringType(), False),
    StructField("black", StringType(), False),
    StructField("result", StringType(), True),
    StructField("white_title", StringType(), True),
    StructField("black_title", StringType(), True),
    StructField("white_elo", LongType(), True),
    StructField("black_elo", LongType(), True),
    StructField("eco", StringType(), True),
    StructField("opening", StringType(), True),
    StructField("variation", StringType(), True),
    StructField("white_fide_id", StringType(), True),
    StructField("black_fide_id", StringType(), True),
    StructField("event_date", DateType(), True),
    StructField("moves", StringType(), True)
])

df_updated = spark.createDataFrame(partidas_df1.rdd, schema)

df_updated.printSchema()


# COMMAND ----------

display(df_updated)

# COMMAND ----------

from pyspark.sql.functions import when, col

# Adicionar a nova coluna 'Result of the match' com base na coluna 'result'
df_updated_with_new_col = df_updated.withColumn(
    "Result of the match",
    when(col("result") == "1/2-1/2", "Draw")
    .when(col("result") == "1-0", "White wins")
    .when(col("result") == "0-1", "Black wins")
    .otherwise("Unknown")
)

# Reorganizar as colunas para colocar 'Result of the match' logo após 'result'
cols = df_updated_with_new_col.columns
new_cols_order = cols[:7] + ['result', 'Result of the match'] + cols[8:]
df_updated_with_new_col2 = df_updated_with_new_col.select(new_cols_order)

# Mostrar o esquema atualizado para verificar se a nova coluna foi adicionada corretamente
df_updated_with_new_col2.printSchema()

# Mostrar as primeiras linhas do DataFrame atualizado para verificar o conteúdo
df_updated_with_new_col2.show()

# COMMAND ----------

from pyspark.sql.functions import col

# Lista de todas as colunas
all_columns = df_updated_with_new_col2.columns

# Remover a duplicata 'Result of the match' na última posição
columns_to_keep = all_columns[:-1]

# Selecionar as colunas desejadas
df_updated_with_new_col2 = df_updated_with_new_col2.select(*columns_to_keep)

# Mostrar o esquema atualizado para verificar as mudanças
df_updated_with_new_col2.printSchema()

# Mostrar algumas linhas para verificar os dados
df_updated_with_new_col2.show()

# COMMAND ----------

display(df_updated_with_new_col2)

# COMMAND ----------

df_updated_with_new_col2.printSchema()

# COMMAND ----------

from pyspark.sql.functions import col, when
from pyspark.sql.types import StructType, StructField, StringType, LongType, DoubleType, DateType, IntegerType

df_updated_with_new_col3 = df_updated_with_new_col2.withColumn(
    'white_fide_id', when(col('white_fide_id').isNull(), 0).otherwise(col('white_fide_id'))
).withColumn(
    'black_fide_id', when(col('black_fide_id').isNull(), 0).otherwise(col('black_fide_id'))
)

# Transformar os tipos de dados e garantir que white_fide_id e black_fide_id sejam não nulos
partidas_df_transform_type = (
    df_updated_with_new_col3
    .withColumn('white_elo', df_updated_with_new_col3['white_elo'].cast('integer'))
    .withColumn('black_elo', df_updated_with_new_col3['black_elo'].cast('integer'))
    .withColumn('white_fide_id', df_updated_with_new_col3['white_fide_id'].cast('integer'))
    .withColumn('black_fide_id', df_updated_with_new_col3['black_fide_id'].cast('integer'))
)

new_schema = StructType([
    StructField("id", LongType(), False),
    StructField("event", StringType(), True),
    StructField("site", StringType(), True),
    StructField("date", DateType(), True),
    StructField("round", DoubleType(), True),
    StructField("white", StringType(), True),
    StructField("black", StringType(), True),
    StructField("result", StringType(), True),
    StructField('Result of the match', StringType(), True),
    StructField("white_title", StringType(), True),
    StructField("black_title", StringType(), True),
    StructField("white_elo", LongType(), True),
    StructField("black_elo", LongType(), True),
    StructField("eco", StringType(), True),
    StructField("opening", StringType(), True),
    StructField("variation", StringType(), True),
    StructField("white_fide_id", StringType(), True),
    StructField("black_fide_id", StringType(), True),
    StructField("event_date", DateType(), True),
    StructField("moves", StringType(), True)
])

partidas_df_transform_type2 = spark.createDataFrame(partidas_df_transform_type.rdd, new_schema)

partidas_df_transform_type2.printSchema()

# COMMAND ----------

display(partidas_df_transform_type2)

# COMMAND ----------

from pyspark.sql.functions import col

partidas_df_transform_type2 = partidas_df_transform_type2.withColumnRenamed("Result of the match", "result_of_match")

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, to_date
from pyspark.sql.types import IntegerType, DateType

# Criando uma sessão Spark (caso ainda não exista)
spark = SparkSession.builder.appName("NullHandling").getOrCreate()

# Supondo que 'partidas_df_transform_type2_filled' já exista com a estrutura fornecida

# Substituindo valores nulos
partidas_df_transform_type2_filled = partidas_df_transform_type2_filled.fillna({
    'event': 'Unknown',
    'site': 'Unknown',
    'round': 0.0,
    'white': 'Unknown',
    'black': 'Unknown',
    'result': 'Unknown',
    'result_of_match': 'Unknown',
    'white_title': 'Unknown',
    'black_title': 'Unknown',
    'white_elo': 0,
    'black_elo': 0,
    'eco': 'Unknown',
    'opening': 'Unknown',
    'variation': 'Unknown',
    'white_fide_id': '0',
    'black_fide_id': '0',
    'moves': 'Unknown'
})

# Convertendo strings de data para DateType e substituindo valores nulos
partidas_df_transform_type2_filled = partidas_df_transform_type2_filled.withColumn(
    "date", when(col("date").isNull(), to_date(lit("1900-01-01"))).otherwise(col("date"))
)
partidas_df_transform_type2_filled = partidas_df_transform_type2_filled.withColumn(
    "event_date", when(col("event_date").isNull(), to_date(lit("1900-01-01"))).otherwise(col("event_date"))
)

# Convertendo colunas white_fide_id e black_fide_id para IntegerType e substituindo valores 'Unknown' por 0
partidas_df_transform_type2_filled = partidas_df_transform_type2_filled.withColumn(
    "white_fide_id", when(col("white_fide_id") == 'Unknown', lit(0)).otherwise(col("white_fide_id").cast(IntegerType()))
).withColumn(
    "black_fide_id", when(col("black_fide_id") == 'Unknown', lit(0)).otherwise(col("black_fide_id").cast(IntegerType()))
)

# Garantindo que as colunas numéricas estejam no formato correto
partidas_df_transform_type2_filled = partidas_df_transform_type2_filled.withColumn(
    "white_elo", col("white_elo").cast(IntegerType())
).withColumn(
    "black_elo", col("black_elo").cast(IntegerType())
)

# Verificando e preenchendo valores nulos em todas as colunas
for column in partidas_df_transform_type2_filled.columns:
    partidas_df_transform_type2_filled = partidas_df_transform_type2_filled.withColumn(
        column, when(col(column).isNull(), lit('Unknown')).otherwise(col(column))
    )


# COMMAND ----------

display(partidas_df_transform_type2_filled)

# COMMAND ----------

# Tentando salvar a tabela novamente
try:
    partidas_df_transform_type2_filled.write.mode('append').saveAsTable('silver.partidas_campeonato')
    print("Table saved successfully.")
except Exception as e:
    print(f"Error while saving table: {e}")
