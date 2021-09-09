import pymysql


class DBClient:
    _url = 'jdbc:mysql://124.70.109.252:3306/test'
    _user = 'root'
    _password = 'MySQL123'
    _sqlStr = 'show databases;'
    _host = '124.70.109.252'
    _port = 3306
    _conn = None

    def __init__(self):
        self._status = False
        print("OPEN")

        # with self._conn:
        #     with self._conn.cursor() as self._cur:
        #         # Read a single record
        #         sql = "SELECT database();"
        #         self._cur.execute(sql)
        #         result = self._cur.fetchall()
        #         print(result)

    def __del__(self):
        if self._conn and self._conn.open:
            self._conn.close()
        print("CLOSE")

    def connect(self, host=_host, port=_port, url=_url, user=_user, password=_password):
        try:
            self._conn = pymysql.connect(host=host,
                                         port=port,
                                         user=user,
                                         password=password,
                                         database='test',
                                         charset='utf8mb4',
                                         connect_timeout=1)
            print("已连接数据库")
            self._status = True
        except pymysql.err.OperationalError as e:
            print("mysql连接失败：", e)
            self._status = False

    def query(self, sql_str: str):
        if self._status:
            cursor = self._conn.cursor()
            cursor.execute(sql_str)
            self._conn.commit()
            result = cursor.fetchall()
            print("query success")
            return result
        else:
            return None

    def status(self):
        return self._status
