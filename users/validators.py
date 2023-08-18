import datetime

from social_twit.settings import ALLOWED_MAIL_DOMAIN


class ValidationPassword():
    def __init__(self, password):
        self.password = password
        self.symbol_isdigit = False
        self.symbol_isalpha = False

    def get_validate_password(self):
        if len(self.password) < 8:
            return False
        else:
            symbol_isdigit = False
            symbol_isalpha = False

            for symbol in self.password:
                if symbol.isdigit():
                    symbol_isdigit = True
                elif symbol.isalpha():
                    symbol_isalpha = True

            if symbol_isalpha and symbol_isdigit:
                return True
            else:
                return False



class ValidationEmail():
    def __init__(self, email):
        self.email = email

    def get_validate_email(self):
        if self.email.split("@")[-1] not in ALLOWED_MAIL_DOMAIN:
            return False
        else:
            return True


class ValidateBirthday():
    def __init__(self, birthday):
        self.birthday = birthday
        self.today = datetime.datetime.now()

    def get_validate_birthday(self):
        if self.birthday.day <= self.today.day and self.birthday.month <= self.today.month:
            delta_year = self.today.year - self.birthday.year
        else:
            delta_year = self.today.year-self.birthday.year-1
        return delta_year >= 18
