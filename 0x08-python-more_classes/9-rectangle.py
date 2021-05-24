#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Initial method """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ defines a rectangle """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ print the rectangle """
        if self.__height == 0 or self.__width == 0:
            return ""
        new = (str(self.print_symbol) * self.__width + '\n') * self.__height
        return new.strip('\n')

    def __repr__(self):
        """ print Rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ print the message Rectangle """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """using property decorator"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter and value validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """using property decorator"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter and value validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_rect_one = rect_1.area()
        area_rect_two = rect_2.area()

        if area_rect_one == area_rect_two or area_rect_one > area_rect_two:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ square is a rectangle """
        return cls(size, size)

    def area(self):
        """ Area Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter Rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            p = 2 * (self.__height + self.__width)
            return p
