import ibm_db2

connection=ibm_db2.connect()
sql="""CREATE TABLE Persons (
    
    name varchar(255),
    phone varchar(255),
    email varchar(255),
    password varchar(255)
);"""

ibm_db2.exec_immediate(connection,sql)

print("DATABASE ADDED SUCCESSFULLY")