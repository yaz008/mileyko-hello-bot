from os import getenv
from re import match

from dotenv import load_dotenv

from project.env.exceptions import (
    DotenvNotFoundError,
    EnvVarMissingError,
    EnvVarValueError,
)


if not load_dotenv():
    raise DotenvNotFoundError


class EnvVar(str):
    def __new__(cls: type, name: str, pattern: str) -> 'EnvVar':
        var: str | None = getenv(key=name)
        if var is None:
            raise EnvVarMissingError(name)
        if not match(pattern, var):
            raise EnvVarValueError(name, pattern)
        return str.__new__(cls, var)
