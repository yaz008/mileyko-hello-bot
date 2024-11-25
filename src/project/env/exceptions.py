from project.exceptions import BaseVexintException


class DotenvNotFoundError(BaseVexintException):
    def __init__(self) -> None:
        super().__init__('Unable to load \".env\" file')


class EnvVarMissingError(BaseVexintException):
    def __init__(self, name: str) -> None:
        super().__init__(f'Evnvironment variable \"{name}\" is missing')


class EnvVarValueError(BaseVexintException):
    def __init__(self, name: str, pattern: str) -> None:
        super().__init__(f'Value of \"{name}\" must match the pattern r\"{pattern}\"')
