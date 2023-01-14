"""This module includes custom exception classes for the wordcount program."""


class FileTooBigError(Exception):
    """
    This class creates an exception for use when a wordcount
    input file exceeds a specified file size.
    """

    def __init__(self, size):
        """Construct class instance with file size attribute."""
        self.size = size

    def __float__(self):
        """Format file size as type float."""
        return self.size


class FileEmptyError(Exception):
    """
    This class creates an exception for use when a wordcount
    input file is empty.
    """
    pass
