import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_table(self, table_name, columns):
        """
        Создает новую таблицу в базе данных.
        :param table_name: Название таблицы.
        :param columns: Список столбцов в формате "column_name column_type".
        """
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        self.cur.execute(query)
        self.conn.commit()

    def insert_row(self, table_name, values):
        """
        Вставляет новую запись в таблицу.
        :param table_name: Название таблицы.
        :param values: Список значений для вставки в формате "(value1, value2, ...)".
        """
        query = f"INSERT INTO {table_name} VALUES {values}"
        self.cur.execute(query)
        self.conn.commit()

    def select_data(self, table_name, columns="*", condition=None):
        """
        Выбирает данные из таблицы.
        :param table_name: Название таблицы.
        :param columns: Список столбцов, которые нужно выбрать. По умолчанию выбираются все столбцы.
        :param condition: Условие для выборки данных. По умолчанию не задано.
        """
        query = f"SELECT {columns} FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cur.execute(query)
        return self.cur.fetchall()

    def getPost(self, postId):
        try:
            self.__cur.execute(f"SELECT title, text FROM content WHERE id = {postId} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД "+str(e))
 
        return (False, False)
    



    def close(self):
        """
        Закрывает соединение с базой данных.
        """
        self.conn.close()

        