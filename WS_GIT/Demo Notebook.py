# Databricks notebook source
print("Hello World!")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello World!"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #Title 1
# MAGIC ## Title 2
# MAGIC ### Title 3
# MAGIC

# COMMAND ----------

# MAGIC %run /Workspace/Users/gopichandun@systechusa.com/Test

# COMMAND ----------

print(name)

# COMMAND ----------

# MAGIC %fs ls /databricks-datasets

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files=dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

print(files)

# COMMAND ----------

display(files)


# COMMAND ----------


