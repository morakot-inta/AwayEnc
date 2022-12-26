import pyodbc

conn = pyodbc.connect(
        "Driver={ODBC Driver 18 for SQL Server};"
        "Server=tcp:srikrung-core-database.public.9f52ec56a378.database.windows.net,3342;"
        "Uid=sqladmin;"
        "Pwd=0ew,jwfhg]p8iy[z,;"
        "Database=TestAlwayEnc;"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
        "ColumnEncryption=Enabled"
        )
cursor = conn.cursor()

cursor.execute('select Idcard from Agent_Data;')
data = cursor.fetchall()
data = str(data)
print(data)
