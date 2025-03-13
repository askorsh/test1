import vk_api 
import psycopg2 
import pandas as pd 
import matplotlib.pyplot as plt 
from datetime import datetime 
from vk_api import VkApi 
from vk_api.exceptions import ApiError 
#TOKEN = ' ' 
vk_session = VkApi(token=TOKEN) 
vk = vk_session.get_api()
#USER_ID = ' ' 
dbname="vk_data", 
user="postgres", 
password=" ", 
host="localhost", 
port="5432" 
) 
cursor = conn.cursor()
def create_table(): 
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS vk_friends ( 
id SERIAL PRIMARY KEY, 
vk_id INT UNIQUE, 
first_name TEXT, 
last_name TEXT, 
city TEXT, 
age INT, 
friend_count INT 
); 
""") 
conn.commit()
def get_friends_data(): 
try: 
friends = vk.friends.get(user_id=USER_ID, fields="bdate,city,first_name,last_name") 
friend_data = [] 
for friend in friends['items']: 
vk_id = friend['id'] 
first_name = friend['first_name'] 
last_name = friend['last_name'] 
city = friend.get('city', {}).get('title', 'Не указан')
bdate = friend.get('bdate', None) 
age = None 
if bdate and len(bdate.split('.')) == 3:  # Проверка формата "дд.мм.гггг" 
birth_year = int(bdate.split('.')[-1]) 
age = datetime.now().year - birth_year 
try: 
friend_count = vk.friends.get(user_id=vk_id)['count'] 
except ApiError: 
friend_count = None  # Некоторые профили могут быть закрыты 
friend_data.append((vk_id, first_name, last_name, city, age, friend_count)) 
return friend_data 
except ApiError as e: 
print(f"Ошибка VK API: {e}") 
return []
def insert_friends_data(friends): 
for friend in friends: 
cursor.execute(""" 
INSERT INTO vk_friends (vk_id, first_name, last_name, city, age, friend_count) 
VALUES (%s, %s, %s, %s, %s, %s) 
ON CONFLICT (vk_id) DO NOTHING; 
""", friend) 
conn.commit()
create_table() 
friends_data = get_friends_data() 
insert_friends_data(friends_data)
cursor.close() 
conn.close() 
