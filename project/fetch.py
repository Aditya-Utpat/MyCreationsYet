import urllib.request,urllib.parse
import json
import ssl
import sqlite3
import time
import datetime

conn = sqlite3.connect('youtube_data.sqlite')
cur = conn.cursor()

#ignore SSL certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cur.executescript('''

CREATE TABLE IF NOT EXISTS videos(
    video_id TEXT,
    title TEXT,
    likes INTEGER,
    dislikes INTEGER,
    views INTEGER,
    date DATE,
    channel_id INTEGER
);
CREATE TABLE IF NOT EXISTS channel(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    youtubeid TEXT,
    name TEXT,
    subscribers INTEGER,
    videocount INTEGER,
    category TEXT,
    retrieved_at DATE
);

''')
API_key = 'AIzaSyD4sbk-jhN5vUG-DC4lVrsKWoGft7YKPTs'
while True:
    name = input('Enter channel name:')
    if len(name) <1 : break
    no_video = int(input('How many videos to retrive'))
    name = name.replace(' ','')
    url = 'https://www.googleapis.com/youtube/v3/channels?'
    parms = dict()
    parms['key'] = API_key
    parms['part'] = 'statistics,snippet'
    parms['forUsername'] = name

    url = url+urllib.parse.urlencode(parms)
    data = urllib.request.urlopen(url,context=ctx).read().decode()
    print('retrived',url)
    data = json.loads(data)
    try:
        channel_id = data['items'][0]['id']
        subscribers = data['items'][0]['statistics']['subscriberCount']
        videocount = data['items'][0]['statistics']['videoCount']
        name = data['items'][0]['snippet']['title']
        print('Retrieved channel info')
    except :
        try:
            data = urllib.request.urlopen('https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q='+name+'&key='+API_key+'&type=channel',context=ctx).read().decode()
            data = json.loads(data)
            channel_id = data['items'][0]['id']['channelId']
            del parms['forUsername']
            parms['id']= channel_id
            url = 'https://www.googleapis.com/youtube/v3/channels?'
            url = url+urllib.parse.urlencode(parms)
            print(url)
            data = urllib.request.urlopen(url,context=ctx).read().decode()
            data= json.loads(data)
            subscribers = data['items'][0]['statistics']['subscriberCount']
            videocount = data['items'][0]['statistics']['videoCount']
            name = data['items'][0]['snippet']['title']
            print('Retrieved channel info')
        except :
            print('Invalid channel name')
            continue

    cur.execute('''SELECT id FROM channel WHERE youtubeid = ? ''',(channel_id,))
    if cur.fetchone() is None:
        cur.execute('''INSERT OR REPLACE INTO channel(youtubeid,name,subscribers,videocount,retrieved_at) VALUES( ? ,?,?,?,? )''',(channel_id,name,subscribers,videocount,str(datetime.datetime.today().strftime ('%d-%b-%Y'))))
        cur.execute('''SELECT id FROM channel WHERE youtubeid = ? ''',(channel_id,))
    else:
        print('channel already in database')
        continue
    channel_table_id = cur.fetchone()[0]
    conn.commit()

    url = 'https://www.googleapis.com/youtube/v3/activities?'
    parms['part']= 'snippet'
    try:
        del parms['forUsername']
    except:
        pass
    parms['maxResults']= no_video
    parms['channelId'] = channel_id
    url = url+urllib.parse.urlencode(parms)
    data = urllib.request.urlopen(url,context=ctx).read().decode()
    print('retrived',url)
    data = json.loads(data)

    ids = []
    for item in data['items']:
        id = item['snippet']['thumbnails']['default']['url']
        id = id[23:id.rfind('/')]
        ids.append(id)
    print('retrived recent activity','len',len(ids))

    parms['part']= 'statistics,snippet'
    del parms['maxResults']
    del parms['channelId']
    for id in ids:
        try:
            parms['id']= id
            url = 'https://www.googleapis.com/youtube/v3/videos?'
            url = url+urllib.parse.urlencode(parms)
            data = urllib.request.urlopen(url,context=ctx).read().decode()
            print(url)
            data = json.loads(data)

            video_id = id
            views = int(data['items'][0]['statistics']['viewCount'])
            likes = int(data['items'][0]['statistics']['likeCount'])
            dislikes = int(data['items'][0]['statistics']['dislikeCount'])
            date = data['items'][0]['snippet']['publishedAt'][:10]
            category = data['items'][0]['snippet']['categoryId']
            title = data['items'][0]['snippet']['title']

            cur.execute(''' INSERT OR IGNORE INTO videos(video_id,likes,dislikes,views,date,channel_id,title) VALUES( ?,?,?,?,?,?,?)''',(video_id,likes,dislikes,views,date,channel_table_id,title))
            conn.commit()
            time.sleep(0.5)
        except:
            print('unable to retrive video info')
            quit()
    print('retrived video info')
    try:
        data = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/videoCategories?key='+API_key+'&part=snippet&id='+category,context=ctx).read().decode()
        data = json.loads(data)
        category = data['items'][0]['snippet']['title']
        cur.execute('UPDATE channel SET category= ? WHERE name = ?',(category,name))
        conn.commit()
    except Exception as e:
        print(e)
conn.close()
