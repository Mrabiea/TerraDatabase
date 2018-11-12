import mysql.connector

dbconfig = {"host": "localhost",
            "user": "root",
            "password": "rabiea",
            "database": "terra",
            "port": "3306"}


def getneighborland(land):
    _SQL = """select Name from land  where LNR in(select N.LNR2 from land 
    L inner join nachbarland N on L.LNR=N.LNR1 where L.Name=%s)"""
    cursor.execute(_SQL, (land,))
    result = cursor.fetchall()
    return result


def getallContinent():
    _SQL = """select Name from kontinent"""
    cursor.execute(_SQL)
    result = cursor.fetchall()
    return result


def getlanguage(land):
    _SQL = """select S.Name from land L inner join gesprochen G on L.LNR=G.LNR 
    inner join sprache S on S.SNR=G.SNR where L.Name=%s"""
    cursor.execute(_SQL, (land,))
    landinfo = cursor.fetchall()
    return landinfo


def getcities(land):
    _SQL = """select O.Name ,O.landesteil from ort O inner join land L on L.LNR=O.LNR where L.Name=%s"""
    cursor.execute(_SQL, (land,))
    landinfo = cursor.fetchall()
    return landinfo


def getalllands(kontinent):
    _SQL = """select L.Name from land L inner join kontinent K on K.KNR=L.KNR where K.Name=%s"""
    cursor.execute(_SQL, (kontinent,))
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

def getthecapital():
    pass