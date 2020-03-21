from server.bo import business_object as bo


class School(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._name = ""
        self._address = ""

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_address(self):
        return self._address

    def set_address(self, value):
        self._address = value

    def __str__(self):
        return "School: {}, {} - {}".format(self.get_id(), self.get_name(), self.get_address())