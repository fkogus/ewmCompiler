class WrongAttributeError (Exception):

    def __init__(self, param, attr, line, column):
        self.message = f"Parameter {param} do not match with attribute {attr} in {line}:{column}"

    def __str__(self):
        return f"WrongAttributeError: {self.message}"