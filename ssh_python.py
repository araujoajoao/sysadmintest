#!/usr/bin/python3

import paramiko
import mysql.connector

address = '20.44.108.125'
username = 'Boss'
password = 'zNT&2a1II8AP'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=address, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command('ifconfig')
stdin.close()
for line in stdout.readlines():
    print(line.replace('\n', ''))


con = mysql.connector.connect(host='localhost',database='db_mysql',user='root',password='321**')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")