#-*- coding:utf8 -*-

import pymysql


##################################
## 连接流程
## 1.打开mysql库
## 2.获取游标
## 3.执行SQL
## [4.处理SQL的执行结果]
## 5.关闭链接，释放资源
##################################
## 链接的语句以及参数
## connection = pymysql.connect(host,user,password,db,port,charset)
##################################



'''
    获取一条数据
'''
def getOne():
    # 获取一个游标
    cursor = db.cursor()

    # 使用execute() 方法执行SQL查询
    cursor.execute('select version()')

    # 使用 fetchone() 获取单条数据
    data = cursor.fetchone()

    # 输出数据
    print(data)

'''
    创建数据表
'''
def createTable():
    cursor = db.cursor()
    # 如果数据库中存在表就预先删除.
    # 由此可见，pymsyql只能执行一条语句，无法执行多条语句
    cursor.execute("drop table if exists test5")
    # 编写好建表语句
    sql = 'create table test5(id int,name varchar(20))'
    # 执行相关命令
    cursor.execute(sql)
    # 获取数据库创建的返回结果
    cursor.execute("show create table test5")
    # 获取一条结果
    data = cursor.fetchone()
    print(data)

'''
    数据库插入操作
'''
def insert2mysql():
    cursor=db.cursor()
    sql='''
        insert into test5 values(1,'huaingood'),
        (2,'hyw')'''
    # 防止插入数据异常
    try:
        cursor.execute(sql)
        db.commit()    # 插入数据时启动事务，防止出错
    except:
        db.rollback()

'''
    从数据库中查询数据
    fetchone()    # 返回一条结果
    fetchall()    # 返回查询的所有结果
    rowcount()    # 返回受影响的行数
'''
def quaryMany():
    cursor = db.cursor()
    sql = '''
        select * from test5
    '''
    try:
        # 返回受影响的行数
        row = cursor.execute(sql)
        # 获取返回的结果
        datas = cursor.fetchall()
        # 遍历输出结果
        for data in datas:
            id = data[0]
            name = data[1]
            print('ID是：'+str(id) +','+'姓名是：'+name)
    except:
        print('无法查询到数据！')


'''
    更新操作
'''
def updateMysql():
    cursor = db.cursor()
    sql='''
        update test5 set id=2 where name='huabingood'
    '''
    try:
        cursor.execute(sql)
    except:
        db.commit()


# 测试链接
if __name__ == '__main__':
    # 打开数据库连接
    db = pymysql.connect('localhost', 'root', '123456', 'my_test')

    # getOne()
    # createTable()
    # insert2mysql()
    quaryMany()

    # 关掉数据库连接
    db.close()
