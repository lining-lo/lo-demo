"""
  @Author:lining-lo
  @Time:2026/6/28
  @Desc:mysql操作
"""
import pymysql


def init_connect():
    conn = pymysql.connect(
        host="localhost",  # 主机地址
        port=3306,  # mysql的端口号
        user="root",  # mysql用户名
        password="123456",  # mysql密码
        database="test01",  # 数据库名称
        charset="utf8",  # 字符集
        cursorclass=pymysql.cursors.DictCursor  # 将查询的结果转化为字典
    )
    print("数据库连接成功！")
    return conn

def sql_execute(conn,sql,args=()):
    cursor = conn.cursor()
    cursor.execute(sql, args)
    result = cursor.fetchall()
    conn.commit()
    print(result)
    print("数据库操作执行成功！")
    cursor.close()
    conn.close()

if __name__ == '__main__':
    conn = init_connect()

    # sql = "INSERT INTO user (username,password) VALUES (%s,%s)"
    # sql_execute(conn,sql,('admin','123456'))

    # sql = "UPDATE user SET password = %s WHERE uid = %s"
    # sql_execute(conn, sql, ('admin', '1'))

    # sql = "DELETE FROM user WHERE uid = %s"
    # sql_execute(conn, sql, (1,))

    sql = "select * from user"
    sql_execute(conn, sql)