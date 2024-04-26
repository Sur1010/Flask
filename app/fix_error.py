import mysql.connector
cnx = mysql.connector.connect(user='root', password='Sur1234',
                              host='127.0.0.1', database='flask_db',
                              auth_plugin='mysql_native_password')
