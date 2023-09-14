from urllib.parse import quote


class dbconfig:
    url = quote('localhost')
    port = quote('3306')
    username = quote('root')
    password =  quote('root')
    mysqldb = quote('dbcpi')

# class dboracleconfig:
#     url = quote('localhost')
#     port = quote('3306')
#     username = quote('CPI')
#     password =  quote('"$Cambodia089$"')
#     port =  quote('1521')
#     db = quote('XE')


class dboracleconfig:
    url = quote('10.20.38.6')
    port = quote('3306')
    username = quote('CPIAPP')
    password =  quote('CPIAPPTEST')
    port =  quote('1521')
    db = quote('CPIDB')