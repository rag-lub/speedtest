import speedtest
import sqlite3
import time
threads = 3
s = speedtest.Speedtest()
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
result = s.results.dict()
for k,v in result.items():
    print(k,v)
conn=sqlite3.connect('speedtestdb.db')
cur=conn.cursor()
#cur.execute('''CREATE TABLE speed_results (DateTimeStamp text, Download real, Upload real, Ping real, ServerAddress text, ServerCity text, ClientIP text, ClientISP text )''')
cur.execute("""INSERT INTO  speed_results VALUES (?,?,?,?,?,?,?,?);""",(result['timestamp'],result['download'],result['upload'],result['ping'],result['server']['host'],result['server']['name'],result['client']['ip'],result['client']['isp']))
conn.commit()
cur.execute("""SELECT * FROM speed_results""")
print(cur.fetchall())
conn.close()
