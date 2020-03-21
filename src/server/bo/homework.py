from server.bo import business_object as bo


class Homework(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._first_name = ""
        self._surname = ""

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        self._first_name = value

    def get_surname(self):
        return self._surname

    def set_surname(self, value):
        self._surname = value

    @staticmethod
    def create(first_name, surname):
        homework = Homework()
        homework.set_first_name(first_name)
        homework.set_surname(surname)
        return homework

    def __str__(self):
        return "Homework: {}, {} {}".format(self.get_id(), self._first_name, self._surname)