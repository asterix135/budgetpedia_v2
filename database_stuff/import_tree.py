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

def main():
    connection = connect()
    with connection.cursor() as cursor:
        sql = 'SELECT * from explorer_lineitem'
        cursor.execute(sql)
        results = cursor.fetchall()
    connection.close()
    print(len(results))

if __name__ == '__main__':
    main()
