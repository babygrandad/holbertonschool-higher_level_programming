#!/usr/bin/python3
"""A module that defines the BaseGeometry class."""

class BaseGeometry:
    """
    A base class for geometry objects, providing basic methods for
    area calculation and integer validation.
    """

    def area(self):
        """
        A method to calculate the area of a geometry object.
        This method is not implemented and should be overridden in
        subclasses.

        Raises:
            Exception: Always raises an exception indicating that the
                       method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer and greater than zero.

        Args:
            name (str): The name of the parameter (for error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
