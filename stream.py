import pymssql
import pandas as pd
server = 'HOWE-ACCT-SERV\SAGE300CRE'
database = 'HoweInc'
user = 'sa'
password = 'L+S3jr3fP@*1'

# Replace 'your_server', 'your_username', 'your_password', and 'your_database' with your SQL Server credentials
connection = pymssql.connect(server=server, user=user, password=password, database=database)

cursor = connection.cursor()
cursor.execute('SELECT JCM_MASTER__JOB.Job, JCM_MASTER__JOB.JTD_Cost FROM JCM_MASTER__JOB')

columns = [column[0] for column in cursor.description]
print(columns)
