import pandas as pd
import sqlite3

df = pd.read_csv("Sport car price.csv")
print(df.head())
print(df.tail())

connection = sqlite3.connect("sportcars")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS sportcars")

df.to_sql("sportcars", connection)

connection.close()


