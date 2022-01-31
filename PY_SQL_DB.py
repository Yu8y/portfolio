#This application will read roster data in JSON format,
#parse the file, and then produce an SQLite database that contains a User, Course, and Member table
#and populate the tables from the data file.

import sqlite3
import json

conn = sqlite3.connect('rosterdatadb.sqlite')
cur = conn.cursor()

fname = input('Enter your file name: ')
if (len(fname) < 1): fname = 'roster_data.json'
fh = open(fname).read() #bytes from file here

#[
  #["Joanne","si110",1],





cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;


CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY(user_id, course_id, role)

)
''')
namecount = dict()
nameslist = list()

datalist = json.loads(fh) #list of lists here
print("LEN::", len(datalist))
for entry in datalist:
    print(entry)
    name = entry[0]
    coursetitle = entry[1]
    role = entry[2]
    nameslist.append(name)
    #print('Name: ', name, 'Course: ', coursetitle, 'Role: ', role)

    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''', (name, ))
    cur.execute('''SELECT id FROM User WHERE name = (?)''', (name, ))
    user_id = cur.fetchone()[0]
    #print('User ID: ', user_id)

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''', (coursetitle, ))
    cur.execute('''SELECT id FROM Course WHERE title = (?)''', (coursetitle, ))
    course_id = cur.fetchone()[0]

    #print('Course ID: ', course_id)

    #cur.execute('''INSERT INTO Member (role) VALUES (?)''', (role, ))
    cur.execute('''INSERT INTO Member (user_id, course_id, role) VALUES (?,?,?)''', (user_id, course_id, role, ))
    print('Course ID: ', course_id, 'User ID: ', user_id, 'Role: ', role)

conn.commit()

#Furtehr lines are checking name duplicates
for name in nameslist:
    namecount[name] = namecount.get(name, 0) + 1

#print(namecount)

newnamelist = list()

for k,v in namecount.items():
    newnamelist.append((v,k))
    descending = sorted(newnamelist, reverse = True)

#print(newnamelist)



#for v,k in descending[:10]:
    #print(k,v)
#print(len(descending))
