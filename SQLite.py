import sqlite3

qry = open('create_table_user.sql', 'r').read()
conn = sqlite3.connect('/path/to/db')
c = conn.cursor()
c.execute(qry)
conn.commit()
c.close()
conn.close()