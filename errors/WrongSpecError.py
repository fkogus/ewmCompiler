class WrongSpecError (Exception):

    def __init__(self, command, line, column):
        self.message = f"Wrong specification for command {command} at {line}:{column}"

    def __str__(self):
        return f"WrongSpecError: {self.message}"