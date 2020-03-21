from server.bo import business_object as bo


class Class(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._students = list()

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_students(self):
        return self._students

    def add_student(self, value):
        self._students.append(value)

    def __str__(self):
        return "Class: {}, {}, Students: {}".format(self.get_id(), self._name, self.get_students())