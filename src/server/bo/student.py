from server.bo import business_object as bo


class Student(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._first_name = ""
        self._last_name = ""

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        self._first_name = value

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, value):
        self._last_name = value

    def __str__(self):
        return "Student: {}, {} {}".format(self.get_id(), self._first_name, self._last_name)