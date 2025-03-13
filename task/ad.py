conn = psycopg2.connect( 
dbname="vk_data", 
user="postgres", 
password="your_password", 
host="localhost", 
port="5432" 
) 
df = pd.read_sql("SELECT age FROM vk_friends WHERE age IS NOT NULL", conn)
plt.figure(figsize=(8, 5)) 
plt.hist(df["age"], bins=10, color="skyblue", edgecolor="black") 
plt.xlabel("Возраст") 
plt.ylabel("Количество друзей") 
plt.title("Распределение возрастов друзей") 
plt.show() 
conn.close()
conn = psycopg2.connect( 
dbname="vk_data", 
user="postgres", 
password="your_password", 
host="localhost", 
port="5432" 
) 
df = pd.read_sql("SELECT city FROM vk_friends", conn) 
city_counts = df["city"].value_counts().head(10) 
plt.figure(figsize=(10, 5)) 
city_counts.plot(kind="bar", color="lightcoral") 
plt.xlabel("Город") 
plt.ylabel("Количество друзей") 
plt.title("Распределение друзей по городам") 
plt.xticks(rotation=45) 
plt.show() 
conn.close()