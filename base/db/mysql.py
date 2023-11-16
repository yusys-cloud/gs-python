import pymysql

# MySQL数据库连接配置
config = {
    'user': 'root',
    'password': 'admin',
    'host': 'localhost',
    'database': 'demo'
}

# 创建数据库
def create_database(database_name):
    conn = None
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"数据库 {database_name} 创建成功")
    except pymysql.Error as error:
        print(f"创建数据库失败: {error}")
    finally:
        if conn and conn.open:
            cursor.close()
            conn.close()

# 读取SQL文件
def read_sql_file(filename):
    with open(filename, 'r') as file:
        sql_statements = file.readlines()
    return sql_statements

# 执行INSERT INTO语句
def execute_insert_statements(sql_statements):
    conn = None
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        
        for statement in sql_statements:
            if statement.strip():
                cursor.execute(statement)
        
        conn.commit()
        print("插入成功")
    except pymysql.Error as error:
        print("插入失败: {}".format(error))
    finally:
        if conn and conn.open:
            cursor.close()
            conn.close()

create_database('demo')

# 读取SQL文件中的INSERT INTO语句并执行插入
sql_file = '/home/ubuntu/xd-20230707.sql'
insert_statements = read_sql_file(sql_file)
execute_insert_statements(insert_statements)