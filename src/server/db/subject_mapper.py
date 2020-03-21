from server.bo.subject import Subject
from server.db.mapper import Mapper


class SubjectMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from subject")
        tuples = cursor.fetchall()

        for (id, name) in tuples:
            subject = Subject()
            subject.set_id(id)
            subject.set_name(name)
            result.append(subject)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, name FROM subject WHERE name LIKE '{}' ORDER BY name".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, first_name, surname) in tuples:
            subject = Subject()
            subject.set_id(id)
            subject.set_name(name)
            result.append(subject)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name FROM subject WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, name) = tuples[0]
            subject = Subject()
            subject.set_id(id)
            subject.set_name(name)
            result = subject
        except IndexError:
            """tritt auf, wenn kein Tupel zurückgeliefert wurde"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, subject):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM subject ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            subject.set_id(maxid[0]+1)

        command = "INSERT INTO subject (id, name) VALUES (%s,%s)"
        data = (subject.get_id(), subject.get_name())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return subject

    def update(self, subject):
        cursor = self._cnx.cursor()

        command = "UPDATE subject " + "SET name=%s WHERE id=%s"
        data = (subject.get_name(), subject.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, subject):
        cursor = self._cnx.cursor()

        command = "DELETE FROM subject WHERE id={}".format(subject.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


if __name__ == "__main__":
    with SubjectMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)