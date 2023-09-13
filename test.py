# import cx_Oracle
# import os

# cx_Oracle.init_oracle_client(lib_dir=r"C:/instantclient_21_10")

# # print(f'os.environ["PATH"]: {os.environ["PATH"]}')
# # print(f'os.system("where oci.dll"): {os.system("where oci.dll")}')

# print("cx_Oracle.version:", cx_Oracle.version)
# print("cx_Oracle.clientversion:", cx_Oracle.clientversion())

# from config.cypertext import cypertext

# cyper = cypertext()
# key ,password = cyper.encrypt("cpi")


# print(str(key))
# print(key.decode())

from config.timestramp import convertdate
 
 
 
print(convertdate.convertotimestamp())