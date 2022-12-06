import mysql.connector
from faker import Faker

fake=Faker()
connection = mysql.connector.connect(
    user='root',
    password='root',
    host='percona',
    port="3306",
    database='db'
)
print("DB conectada")

cursor=connection.cursor()
#CREAR LA TABLA
cursor.execute('CREATE TABLE IF NOT EXISTS estudiantes(id int not null AUTO_INCREMENT,Nombre varchar(100) NOT NULL,Apellido varchar(100) NOT NULL,PRIMARY KEY (id))')

try:
    #METEMOS DATOS
    nombre, apellido=fake.name().split()
    sql='INSERT INTO estudiantes(Nombre, Apellido)VALUES(%s,%s)'
    val=(nombre, apellido)
    cursor.execute(sql,val)
    connection.commit()
except:
    print("?")

#COMPROBAMOS LOS DATOS
cursor.execute('Select * FROM estudiantes')
students = cursor.fetchall()
print(students)

#CERRAMOS CONEXION
connection.close

