conn = psycopg2.connect( 
dbname="social_research", 
user="postgres", 
password="your_password", 
host="localhost", 
port="5432" 
) 
df = pd.read_sql("SELECT answer FROM responses", conn)
top_answers = df["answer"].value_counts().head(10)
plt.figure(figsize=(10, 5)) 
top_answers.plot(kind="bar", color="lightcoral") 
plt.xlabel("Ответ") 
plt.ylabel("Частота") 
plt.title("Наиболее популярные ответы респондентов") 
plt.xticks(rotation=45) 
plt.show() 
conn.close()
