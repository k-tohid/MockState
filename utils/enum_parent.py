from enum import Enum


class EnumParent(Enum):
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def values(cls):
        return [key.value for key in cls]

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return str(self.key)
