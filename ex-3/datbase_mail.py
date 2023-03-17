import sqlite3

conn = sqlite3.connect('DATA.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

Filename = input('Enter file name:')
File = open(Filename)
count= 0
for line in File:
    if line.startswith('From: '):
        line = line.split()
        email = line[1].split('@')[1]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (email,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email,))
        if count == 10:
            conn.commit()
            count=0
        count= count+1

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
