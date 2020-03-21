from server.bo import business_object as bo
import datetime


class Homework(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._file_path = ""
        self._description = ""
        self._start_event = datetime.datetime.now()
        self._end_event = datetime.datetime.now()
        self._subject_id = 0
        self._school_class_id = 0

    def get_file_path(self):
        return self._file_path

    def set_file_path(self, value):
        self._file_path = value

    def get_description(self):
        return self._description

    def set_description(self, value):
        self._description = value

    def get_start_event(self):
        return self._start_event

    def set_start_event(self, value):
        self._start_event = value

    def get_end_event(self):
        return self._end_event

    def set_end_event(self, value):
        self._end_event = value

    def get_subject_id(self):
        return self._subject_id

    def set_subject_id(self, value):
        self._subject_id = value

    def get_school_class_id(self):
        return self._school_class_id

    def set_school_class_id(self, value):
        self._school_class_id = value

    @staticmethod
    def create(description):
        homework = Homework()
        homework.set_description(description)
        return homework

    def __str__(self):
        return "Homework: {}, {} {} - {} - {}".format(self.get_id(), self.get_file_path(), self.get_description(),
                                                      self.get_start_event(), self.get_end_event())
