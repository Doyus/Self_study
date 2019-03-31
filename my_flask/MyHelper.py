import pymysql
class MyHelper:

    def __init__(self,host,name,pwd,database):
        self.host = host
        self.name = name
        self.pwd = pwd
        self.database = database


    def getConn(self):
        self.conn = pymysql.connect(self.host,self.name,self.pwd,self.database)
        self.cursor = self.conn.cursor()
    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print(e)

    def queryAll(self,sql,params=()):
        result = ()
        self.getConn()
        try:
            self.cursor.execute(sql,params)
            # print(sql)

            result = self.cursor.fetchall()
            # print(params)
            # print(result)
            self.close()
        except Exception as e:
            print(e)
        return result
    def queryOne(self,sql,params=()):
        result = ()
        self.getConn()
        try:
            self.cursor.execute(sql,params)
            # print(sql)
            # print(params)
            result = self.cursor.fetchone()
            # print(result)
            self.close()
        except Exception as e:
            print(e)

        return result

    def exe(self,sql):
        self.getConn()

        self.cursor.execute(sql)
        self.conn.commit()
            # print(sql)
        self.close()

        print('操作成功')





# def queryAll(self,sql,params=()):
#         result = ()
#         self.getConn()
#         try:
#             self.cursor.execute(sql,params)
#             print(sql)

#             result = self.cursur.fetchall()
#             print(params)
#             print(result)
#             self.close()
#         except Exception as e:
#             print(e)
#         return result
