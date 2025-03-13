import psycopg2 
import pandas as pd 
import matplotlib.pyplot as plt
conn = psycopg2.connect( 
dbname="social_research", 
user="postgres", 
password="your_password", 
host="localhost", 
port="5432" 
) 
df = pd.read_sql("SELECT age FROM respondents", conn)
plt.figure(figsize=(8, 5)) 
plt.hist(df["age"], bins=10, color="skyblue", edgecolor="black") 
plt.xlabel("Возраст") 
plt.ylabel("Количество респондентов") 
plt.title("Распределение возрастов респондентов") 
plt.show() 
conn.close()