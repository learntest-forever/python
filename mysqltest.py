import pymysql


class mysql():
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.__conn = pymysql.connect(self.host, self.user, self.password, self.database,
                                      charset='utf8', cursorclass=pymysql.cursors.DictCursor)

    def sql_exec(self, command):
        # logging.debug(f"mysql query, sql: {sql}")
        result = None
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(command)
                result = cursor.fetchall()
                self.__conn.commit()
                cursor.close()
                # self.__conn.close()
        except pymysql.err.OperationalError as e:
            print(f"mysql query error, unable to fetch data, {e}")
        except pymysql.err.Error as e:
            print(f"mysql query error, {e}")
        return result


if __name__ == '__main__':
    host = '10.170.124.33'
    #host = '192.168.20.50'
    user = "root"
    password = "1234567890///"
    database = "tes"
    db = mysql(host=host, user=user, password=password, database=database)
    #command1 = f'INSERT INTO	config  VALUES(10,"\"1234568\"","","","","");'
    command1 = 'INSERT INTO	config  VALUES(10,"\\"1234568\\"","","","","");'
    result = db.sql_exec(command1)

