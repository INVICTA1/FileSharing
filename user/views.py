from django.shortcuts import render

import pymysql.cursors

connection = pymysql.connect(
    host='127.0.0.1',
    user='admin',
    password='admin',
    database='filesharing',
)
try:
    with connection.cursor() as cursor:
        def choose_table():
            tables = {}
            i = 1
            cursor.execute('SHOW tables')
            print('Tables:')
            for table in cursor:
                print(i, '-', table[0])
                tables[i] = table[0]
                i += 1
            num = int(input('Enter table:'))
            return tables[num]


        def show_description(table):
            field_names = {}
            i = 1
            cursor.execute('select * from {0}'.format(table))
            fields = cursor.description
            print("The table field names:")
            for field in fields:
                print(field[0], end=' ')
                field_names[field[0]] = ''
                i += 1
            print('')
            return field_names


        def add_user(table, field_names):
            key = ''
            value = ''
            if "id" in field_names:
                del field_names['id']
            for i in field_names:
                field_names[i] = input('Enter ' + i + ':')
            for i, j in field_names.items():
                key = key + str(i) + ','
                value = value + "'" + str(j) + "'" + ','
            insert_data = 'insert into {0}({1}) values ({2});'.format(table, key[:-1], value[:-1])
            try:
                cursor.execute(insert_data)
                connection.commit()
            except :
                print('this person is exist')


        def conditions(table, field_names):

            i = 1
            condition = []
            while True:
                for key, value in field_names.items():
                    print(str(i) + ')' + key + ':' + value)
                    i += 1
                changes = (input("Enter restrictions, example: id=1,name=Misha,press enter when done\n"))
                if changes == '':
                    break
                else:
                    condition.append(changes)
            return condition


        def read_users(table, field_names):
            num = int(input('1)Read one user\n'
                            '2)Read all users\n'
                            '3)Back\n'))
            change_values = {}
            a = ''
            if num == 1:
                condition = conditions(table, field_names)
                if len(condition) > 1:
                    for i in condition:
                        a += i + ' and '
                elif len(condition) == 1:
                    a += condition[0]
                # print(a)
                show_users = 'select * from {0} where {1};'.format(table,
                                                                   a)  # значение должно быть в кавычках при запросе

            elif num == 2:
                show_users = 'select * from {0};'.format(table)
            elif num == 2:
                return menu()
            else:
                return read_users()
            cursor.execute(show_users)
            fields = cursor.description
            for field in fields:
                print(field[0], end=' ')
            for i in cursor:
                print()
                for j in i:
                    print(j, end=' ')


        def update_user(table, field_names):
            change_data = input("Enter data")
            conditions = input("Enter conditions")

            update_base_sql = 'update {0} set {1} where {2};'.format(table, change_data, conditions)
            cursor.execute(update_base_sql)
            connection.commit()


        def delete_user(table, field_names):
            delete_user_sql = "delete from {0} where {1}".format(table, conditions(table,field_names))
            print(delete_user_sql)
            cursor.execute(delete_user_sql)
            connection.commit()


        menu_tables = {1: add_user,
                       2: read_users,
                       3: update_user,
                       4: delete_user,
                       }


        def menu():
            table = choose_table()
            field_names = show_description(table)
            # add_user(table, field_names)работает
            # restriction(field_names)
            while True:
                num = int(input("\n1)Add user\n"
                                "2)Read users\n"
                                "3)Update user\n"
                                "4)Delete user\n"
                                "5)Exit\n"))
                if num == 5:
                    break
                menu_tables[num](table, field_names)


        # try:
        #     menu()
        # except KeyError:
        #     print("wrong data selected")
        # finally:
        menu()

finally:
    cursor.close()
