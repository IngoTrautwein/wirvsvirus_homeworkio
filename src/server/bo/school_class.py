from server.bo import business_object as bo


class SchoolClass(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._name = ""

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def __str__(self):
        return "SchoolClass: {}, {}, Students: {}".format(self.get_id(), self._name)