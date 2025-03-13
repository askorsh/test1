conn = psycopg2.connect( 
dbname="vk_data", 
user="postgres", 
password="your_password", 
host="localhost", 
port="5432" 
) 
df = pd.read_sql("SELECT age, friend_count FROM vk_friends WHERE age IS NOT NULL 
AND friend_count IS NOT NULL", conn)
 plt.figure(figsize=(8, 5)) 
plt.scatter(df["age"], df["friend_count"], alpha=0.5, color="blue") 
plt.xlabel("Возраст") 
plt.ylabel("Количество друзей") 
plt.title("Корреляция возраста и количества друзей") 
plt.show() 
conn.close()