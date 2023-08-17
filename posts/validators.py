import datetime

from social_twit.settings import STOP_LIST_WORDS



class ValidationBirthday():
    def __init__(self, birthday):
        self.birthday = birthday
        self.today = datetime.datetime.now()

    def get_validate_birthday(self):
        if self.birthday.day <= self.today.day and self.birthday.month <= self.today.month:
            delta_year = self.today.year - self.birthday.year
        else:
            delta_year = self.today.year-self.birthday.year-1
        return delta_year >= 18


class ValidationWords():
    def __init__(self, words):
        self.words = words.lower()

    def get_validate_words(self):
        for word in STOP_LIST_WORDS:
            if word in self.words:
                return False
        return True