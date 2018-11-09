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
    # return cursor.fetchall()


def getalllands():
    _SQL = """select Name from land"""
    cursor.execute(_SQL)
    result = cursor.fetchall()
    return result


def getlandinfo(land):
    _SQL="""select * from land where Name=%s"""
    cursor.execute(_SQL, (land,))
    landinfo =cursor.fetchall()
    return landinfo

def connectto_database():
    global dbconfig, connection, cursor
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
