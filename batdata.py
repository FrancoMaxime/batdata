import csv
import os
import sqlite3

DBNAME = "data_chiroptere.sqlite"
conn = None
db = None

print("Generation Database file")
conn= sqlite3.connect(DBNAME)
db = conn.cursor()
with open('schema.sql') as f:
    db.executescript(f.read())
conn.commit()

total = 0
total_egal = 0
for x in os.listdir('./csv'):
    print('file '+ x + '.....')
    with open('./csv/' + x) as csv_file, open('result/result_' + x, 'w') as result:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        print(csv_reader.fieldnames)
        writer = csv.DictWriter(result, fieldnames=csv_reader.fieldnames)
        writer.writeheader()
        for row in csv_reader:
            if row['Validation'] != '' and row['Id'] != 'parasi' and row['Id'] != 'Parasi':
                total += 1
                writer.writerow(row)
                calls = 0
                if 'NbCalls' in row :
                    calls = row['NbCalls']
                elif 'NbCris' in row:
                    calls = row['NbCris']
                check1 = db.execute('SELECT id_chiroptere from chiroptere where name = ?', (row['Id'],)).fetchone()
                if check1 is None:
                    db.execute('INSERT INTO chiroptere(name, nb_file, nb_call) VALUES '
                               '(?, 0, 0)',(row['Id'],))
                    conn.commit()
                check2 = db.execute('SELECT id_place from place where name = ?', (row['Site'],)).fetchone()
                if check2 is None:
                    db.execute('INSERT INTO place(name) VALUES '
                               '(?)',(row['Site'],))
                    conn.commit()
                
                if calls != 0:
                    db.execute('UPDATE chiroptere SET nb_file = nb_file + 1, nb_call = nb_call + (?) '
                               'WHERE name = ?', (calls, row['Id']))
                if 'Id_avant validation' in row :
                    if row['Id'] == row['Id_avant validation']:
                        total_egal += 1
                elif 'Species' in row :
                    if row['Id'] == row['Species']:
                        total_egal += 1
                    
        print('Done')
        conn.commit()


      
result = db.execute('SELECT name, nb_file, nb_call FROM chiroptere WHERE nb_file >0 ORDER BY nb_file ASC').fetchall()
print(len(result))
with open('result.txt', 'w') as r:
    r.write("name\tnb_file\tnb_call\n")
    for e in range(len(result)):
        r.write(str(result[e][0]) + "\t" + str(result[e][1]) + "\t" + str(result[e][2]) + "\n" )


print(total)
print (total_egal)
