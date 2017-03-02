from .exceptions import InvalidIconTypeError


class IconType(object):
    def __init__(self, os_type, size, description=None):
        field_size = 4
        if len(os_type) != field_size:
            raise InvalidIconTypeError()

        self.os_type = os_type
        self.size = size
        self.description = description

    def as_bytearray(self):
        """
        +-----------------------------+
        | Octet       |       0       |
        | Bit         | 0 | 1 | 2 | 3 |
        +-------------+---------------+
        | Description |     OSType    |
        +-----------------------------+
        """
        return bytearray(self.os_type, encoding='ascii')
