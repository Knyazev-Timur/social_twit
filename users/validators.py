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
