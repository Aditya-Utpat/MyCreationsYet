import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('relation.sqlite')
cur = conn.cursor()

cur.executescript('''

DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)

''')

file = input('Enter file name:')
file = open(file).read()
xml = ET.fromstring(file)
tracks = xml.findall('dict/dict/dict')



commitment = 0
for track in tracks:
    for i in range(len(track)):
        if track[i].text == 'Name':
            name = track[i+1].text
        elif track[i].text == 'Artist':
            artist= track[i+1].text
        elif track[i].text == 'Album':
            album= track[i+1].text
        elif track[i].text == 'Genre':
            genre= track[i+1].text
        elif track[i].text == 'Rating':
            rating=track[i+1].text
        elif track[i].text == 'Play Count':
            count= track[i+1].text
        elif track[i].text == 'Total Time':
            length= track[i+1].text

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', (genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count,genre_id)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( name, album_id, length, rating, count, genre_id, ) )

    if commitment == 10:
        conn.commit()
        commitment = 0
    commitment += 1
conn.commit()
