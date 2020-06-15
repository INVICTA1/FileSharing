from django.contrib import admin

# Register your model here.
import pymysql.cursors


def get_id(id):
    connection = pymysql.connect(
        host='127.0.0.1',
        user='admin',
        password='admin',
        database='filesharing',
    )
    try:
        with connection.cursor() as cursor:
            file = {}
            value = []
            num = 0
            id = 'id=' + str(id)
            table = 'file'
            select_file_by_id = 'select * from {0} where {1}'.format(table, id)
            cursor.execute(select_file_by_id)
            fields = cursor.description
            # for field in fields:
            #     print(field[0], end=' ')
            # for i in cursor:
            #     print()
            #     for j in i:
            #         print(j, end=' ')
            for i in cursor:
                print()
                for j in i:
                    value.append(j)
            for field in fields:
                file[field[0]] = value[num]
                num += 1


    finally:
        cursor.close()
    return file
