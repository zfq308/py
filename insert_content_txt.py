import os
import operator
import MySQLdb
import httplib
import time
import sys

def insert(temp, conn):
    sql = "insert into jc_content_txt (content_id, `txt`) values (%s, 'testfjaskldjf;ladfajkshkdjdjjjjjjjjjjjjjjjjjjjjjjjj')"
    cursor = conn.cursor()
    cursor.execute(sql, (temp))
    conn.commit()
	
	

if __name__ == '__main__':
	conn = MySQLdb.connect(host='localhost', user='root',passwd='Uat123', db='cyou')
	i = 2
	while i < 10000 :
		print i
		insert(i, conn)
		i += 1
