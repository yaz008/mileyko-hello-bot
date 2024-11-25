from json import load
from os import listdir
from typing import Callable, Any

from project.cfg.exceptions import UnknownOptionError, InvalidOptionTypeError


def config[T](filename: str) -> Callable[[type[T]], type[T]]:
    def decorator(cls: type[T]) -> type[T]:
        if f'{filename}.json' in listdir('configs'):
            with open(
                file=f'configs\\{filename}.json', mode='r', encoding='UTF-8'
            ) as config_file:
                cfg: dict[str, Any] = load(config_file)
            unknown_keys: set[str] = cfg.keys() - cls.__annotations__.keys()
            if len(unknown_keys) > 0:
                raise UnknownOptionError(filename, unknown_keys)
            for varname, vartype in cls.__annotations__.items():
                new_value: Any = cfg.get(varname, getattr(cls, varname))
                if not isinstance(new_value, vartype):
                    raise InvalidOptionTypeError(filename, varname, vartype)
                setattr(cls, varname, new_value)
        return cls

    return decorator
