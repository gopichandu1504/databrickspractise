# Databricks notebook source
print("Hello World!")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello World From SQL!!" 

# COMMAND ----------

# MAGIC %run /Workspace/Users/gopichandun@systechusa.com/Setup

# COMMAND ----------

print(name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files=dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

display(files)
