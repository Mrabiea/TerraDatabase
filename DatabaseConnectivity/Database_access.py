import mysql.connector

dbconfig = {"host": "localhost",
            "user": "root",
            "password": "rabiea",
            "database": "terra",
            "port": "3306"}


def getallContinent():
    _SQL = """select Name from kontinent"""
    cursor.execute(_SQL)
    result = cursor.fetchall()
    return result

def getlanguage(land):
    _SQL = """select S.Name,L.Name from land L inner join gesprochen G on L.LNR=G.LNR 
    inner join sprache S on S.SNR=G.SNR where L.Name=%s"""
    cursor.execute(_SQL, (land,))
    landinfo = cursor.fetchall()
    return landinfo

def getcities(land):
    _SQL = """select O.Name from ort O inner join land L on L.LNR=O.LNR where L.Name=%s"""
    cursor.execute(_SQL, (land,))
    landinfo = cursor.fetchall()
    return landinfo

def getalllands():
    _SQL = """select Name from land"""
    cursor.execute(_SQL)
    result = cursor.fetchall()
    return result


def getlandinfo(land):
    _SQL = """select * from land where Name=%s"""
    cursor.execute(_SQL, (land,))
    landinfo = cursor.fetchall()
    return landinfo


def connectto_database():
    global dbconfig, connection, cursor
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
