import pymysql.cursors

def connect():
    """
    helper function to connect to database
    :return: mysql connection
    """
    connection = pymysql.connect(host='localhost',
                                 password='budgetpedia',
                                 user='budgetpedia',
                                 db='budgetpedia')
    return connection

connect()
