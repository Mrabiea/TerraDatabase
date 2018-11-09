import mysql.connector

dbconfig = {"host": "localhost",
            "user": "root",
            "password": "rabiea",
            "database": "terra",
            "port": "3306"}


def getallContinent():
    _SQL = """select * from kontinent"""
    result = cursor.execute(_SQL)
    return result
    # return cursor.fetchall()


def getllland():
    _SQL = """select * from land"""
    result = cursor.execute(_SQL)
    return result


def connectto_database():
    global dbconfig, connection, cursor
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
