import sqlite3

conn = sqlite3.connect('youtube_data.sqlite')
cur = conn.cursor()

print('video stats')
cur.execute(''' SELECT title,channel_id,views FROM videos ORDER BY views DESC LIMIT 1''')
most_view = cur.fetchone()
cur.execute('''SELECT name FROM channel WHERE id = ? ''',(most_view[1],))
print('Most viewed video of all :\n'+most_view[0]+'   ===   '+str(most_view[2])+' views   ===   '+cur.fetchone()[0]+'\n')

cur.execute(''' SELECT title,channel_id,likes FROM videos ORDER BY likes DESC LIMIT 1''')
most_view = cur.fetchone()
cur.execute('''SELECT name FROM channel WHERE id = ? ''',(most_view[1],))
print('Most liked video of all :\n'+most_view[0]+'   ===   '+str(most_view[2])+' likes   ===    '+cur.fetchone()[0]+'\n')

cur.execute(''' SELECT title,channel_id,dislikes FROM videos ORDER BY dislikes DESC LIMIT 1''')
most_view = cur.fetchone()
cur.execute('''SELECT name FROM channel WHERE id = ? ''',(most_view[1],))
print('Most disliked video of all :\n'+most_view[0]+'    ===    '+str(most_view[2])+' dislikes   ===   '+cur.fetchone()[0]+'\n')

cur.execute(''' SELECT title,channel_id,date FROM videos ORDER BY date ASC LIMIT 1''')
most_view = cur.fetchone()
cur.execute('''SELECT name FROM channel WHERE id = ? ''',(most_view[1],))
print('Oldest video of all :\n'+most_view[0]+'    ===    '+str(most_view[2])+'   ===   '+cur.fetchone()[0]+'\n')

cur.execute('''SELECT name,subscribers FROM channel ORDER BY subscribers DESC LIMIT 1''')
a = cur.fetchall()
print('channel with most subscribers:\n'+a[0][0]+'===   subscribers   ===   '+str(a[0][1])+'\n')

cur.execute('''SELECT name,videocount FROM channel ORDER BY videocount DESC LIMIT 1''')
a = cur.fetchall()
print('channel with most videocount:\n'+a[0][0]+'===   videos   ===   '+str(a[0][1])+'\n')

conn.close()
