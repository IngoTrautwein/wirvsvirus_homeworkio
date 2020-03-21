from server.bo.homework import Homework
from server.db.mapper import Mapper


class HomeworkMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from homework")
        tuples = cursor.fetchall()

        for (id, description, file_path, start_event, end_event) in tuples:
            homework = Homework()
            homework.set_id(id)
            homework.set_description(description)
            homework.set_file_path(file_path)
            homework.set_start_event(start_event)
            homework.set_end_event(end_event)
            result.append(homework)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, description, file_path, start_event, end_event FROM homework WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, description, file_path, start_event, end_event) = tuples[0]
            homework = Homework()
            homework.set_id(id)
            homework.set_description(description)
            homework.set_file_path(file_path)
            homework.set_start_event(start_event)
            homework.set_end_event(end_event)
            result = homework
        except IndexError:
            """tritt auf, wenn kein Tupel zurückgeliefert wurde"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, homework):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM homework ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            homework.set_id(maxid[0]+1)

        command = "INSERT INTO homework (id, description, file_path, start_event, end_event) VALUES (%s,%s,%s,%s,%s)"
        data = (homework.get_id(), homework.get_description(), homework.get_file_path(), homework.get_start_event(), homework.get_end_event())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return homework

    def update(self, homework):
        cursor = self._cnx.cursor()

        command = "UPDATE homework " + "SET description=%s, file_path=%s, start_event=%s, end_event=%s WHERE id=%s"
        data = (homework.get_description(), homework.get_file_path(), homework.get_start_event(), homework.get_end_event(), homework.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, homework):
        cursor = self._cnx.cursor()

        command = "DELETE FROM homework WHERE id={}".format(homework.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


if __name__ == "__main__":
    with HomeworkMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)