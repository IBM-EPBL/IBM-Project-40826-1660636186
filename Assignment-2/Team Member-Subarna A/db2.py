import ibm_db2

connection=ibm_db2.connect("hostname": "0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud")
sql="""CREATE TABLE Persons (
    
    name varchar(255),
    phone varchar(255),
    email varchar(255),
    password varchar(255)
);"""

ibm_db2.exec_immediate(connection,sql)

print("DATABASE ADDED SUCCESSFULLY")