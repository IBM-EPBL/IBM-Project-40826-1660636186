import ibm_db

connection=ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31505;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=plq76207;PWD=ZmeqbSx0vyVOuxoG",'','')

print(connection)

print("connection successfully...")

sql=""" CREATE TABLE CUSTOMERS(
   name varchar(255),
   address varchar(255) ,
   city varchar(255) ,
   phonenumber varchar(255) ) """

ibm_db.exec_immediate(connection,sql)