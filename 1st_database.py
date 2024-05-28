import sqlite3

connection_string=sqlite3.connect("user.db")
cursor=connection_string.cursor()

table_creation="CREATE TABLE IF NOT EXISTS user(name TEXT, father_name TEXT, mother_name TEXT ,age INTEGER, class INTEGER, section TEXT, roll INTEGER)"
cursor.execute(table_creation)

cursor.execute("INSERT INTO user VALUES('Wasif','Harun','Neera',19,'Honours','N/A',12)")
cursor.execute("INSERT INTO user VALUES('Kaif','Ajmal','Rabeya',15,'Nine','D',23)")
cursor.execute("INSERT INTO user VALUES('Saiful','Ehsan','Tania',12,'Six','A',15)")
cursor.execute("INSERT INTO user VALUES('Sami','Shahid','Rehena',10,'Four','B',32)")
cursor.execute("INSERT INTO user VALUES('Rayhan','Faisal','Sabiha',14,'Eight','E',54)")
connection_string.commit()