import mysql.connector
import sys

search_name = sys.argv[1]

cnx = mysql.connector.connect(user='dsci551', password='Dsci-551'
        , database='sakila', auth_plugin='mysql_native_password')
cursor = cnx.cursor(buffered=True)

query = ("SELECT c.first_name, c.last_name, ct.city FROM customer AS c INNER JOIN address AS a ON c.address_id = a.address_id INNER JOIN city AS ct ON a.city_id =ct.city_id WHERE c.first_name LIKE '%" +search_name+"%';")

cursor.execute(query)

for f_name in cursor:
    print(f_name)

cursor.close()
cnx.close()