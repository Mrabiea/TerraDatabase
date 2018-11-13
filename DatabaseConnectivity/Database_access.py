import mysql.connector

dbconfig = {"host": "localhost",
            "user": "root",
            "password": "rabiea",
            "database": "terra",
            "port": "3306"}


def getneighborland(land):
    '''function to get the neighbors of a selected country'''
    _SQL = """select Name from land  where LNR in(select N.LNR2 from land 
    L inner join nachbarland N on L.LNR=N.LNR1 where L.Name=%s)"""
    cursor.execute(_SQL, (land,))
    result = cursor.fetchall()
    return result


def getallContinent():
    '''function to get all continents. We need it for the first OptionMenu'''
    _SQL = """select Name from kontinent"""
    cursor.execute(_SQL)
    result = cursor.fetchall()
    return result


def getlanguage(land):
    '''function to get all the languages spoken in a selected country'''
    _SQL = """select S.Name from land L inner join gesprochen G on L.LNR=G.LNR 
    inner join sprache S on S.SNR=G.SNR where L.Name=%s"""
    cursor.execute(_SQL, (land,))
    landinfo = cursor.fetchall()
    return landinfo


def getcities(land):
    '''function to get all the cities of a selected country'''
    _SQL = """select O.Name ,O.landesteil,o from ort O inner join land L on L.LNR=O.LNR where L.Name=%s"""
    cursor.execute(_SQL, (land,))
    landinfo = cursor.fetchall()
    return landinfo


def getalllands(kontinent):
    '''function to get all the countries of a selected kontinent.
    We need it for the second DropDown --> Choose a country'''
    _SQL = """select L.Name from land L inner join kontinent K on K.KNR=L.KNR where K.Name=%s"""
    cursor.execute(_SQL, (kontinent,))
    result = cursor.fetchall()
    return result


def getlandinfo(land):
    '''function to get all the information about a selected country'''
    _SQL = """select * from land where Name=%s"""
    cursor.execute(_SQL, (land,))
    landinfo = cursor.fetchall()
    return landinfo

def getortinfo(ort):
    '''function to get all the information needed of a
    selected city in a selected country'''
    _SQL = """select O.Name ,O.landesteil, O.Einwohner, O.Breite, O.Laenge 
    from ort O inner join land L on L.LNR=O.LNR where L.Name=%s"""
    cursor.execute(_SQL, (ort,))
    ortinfo = cursor.fetchall()
    return ortinfo

def connectto_database():
    '''start the connection to the Database and the cursor'''
    global dbconfig, connection, cursor
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()

def getthecapital():
    pass

