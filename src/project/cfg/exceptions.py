from project.exceptions import BaseVexintException


class UnknownOptionError(BaseVexintException):
    def __init__(self, filename: str, unknown_keys: set[str]) -> None:
        error_message: str = ' '.join(
            [
                f'In the file \"configs\\{filename}.json\"',
                'the following options are not recognized:',
                str(list(unknown_keys)),
            ]
        )
        super().__init__(error_message)


class InvalidOptionTypeError(BaseVexintException):
    def __init__(self, filename: str, option_name: str, correct_type: type) -> None:
        error_message: str = ' '.join(
            [
                f'In the file \"configs\\{filename}.json\"',
                f'the option \"{option_name}\" must be of type \"{correct_type}\"',
            ]
        )
        super().__init__(error_message)
