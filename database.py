import psycopg2
import pickle
con = psycopg2.connect(
  database="anova_dev", 
  user="postgres", 
  password="", 
  host="localhost", 
  port="5432"
)
a="""SELECT entry_title, entry_summary ,project_speech."language"  from project_post inner join project_speech ON project_post.feed_language_id = project_speech.id where project_post.feed_language_id in (6,
114,
197,
130,
103,
150,
152,
155,
45,
117) ;"""
b="""SELECT entry_title, entry_summary ,project_speech."language"  from project_post inner join project_speech ON project_post.feed_language_id = project_speech.id where project_post.feed_language_id = 1 """
print("Database opened successfully")
cur = con.cursor()  
cur.execute(a)
rows = cur.fetchall()
with open('arabic.pkl', 'wb') as f:  # open a text file
     pickle.dump(rows, f)
