import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''Generate a random string of lowercase letters of length 15'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student():
    '''A student with a name, surname, active status and id'''
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False, default='Eagle')
    id: str = field(init=False, default_factory=generate_id)
