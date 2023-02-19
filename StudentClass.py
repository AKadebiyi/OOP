from datetime import date


class Student:
    def __init__(self):
        self.__studentid = studentid
        self.__name = name
        self.__dob = dob
        self.__classification = classification
        self.__age = age

    def calc_age(self):
        today = date.today()
        dob = self.__dob.split('/')
        dob_year = int(dob[2])
        age = today.year - dob_year

    def register(self):
        if self.__classification == 'senior':
            self.__register = "11/1 thru 11/3"
        elif self.__classification == 'junior':
            self.__register = "11/4 thru 11/6"
        elif self.__classification == 'sophomore':
            self.__register = "11/7 thru 11/11"
        else:
            self.__register = "classification not found"
        

    def age(self):
        today = date.today()
        age = today - self.__dob

    def get_age(self):
        return age

    def reg_time:
