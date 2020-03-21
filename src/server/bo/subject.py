from server.bo import business_object as bo


class Subject(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._name = ""

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    @staticmethod
    def create(name):
        subject = Subject()
        subject.set_name(name)
        return subject

    def __str__(self):
        return "Subject: {}, {}".format(self.get_id(), self._name)