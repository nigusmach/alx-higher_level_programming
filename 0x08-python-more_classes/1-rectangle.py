#!/usr/bin/python3

# 1-rectangle.py

# Brennan D Baraban <375@holbertonschool.com>

"""Defines a Rectangle class."""





class Rectangle:

        """Represent a rectangle."""



            def __init__(self, width=0, height=0):

                        """Initialize a new Rectangle.

                                Args:

                                            width (int): The width of the new rectangle.

                                                        height (int): The height of the new rectangle.

                                                                """

                                                                        self.width = width

                                                                                self.height = height



                                                                                    @property

                                                                                        def width(self):

                                                                                                    """Get/set the width of the rectangle."""

                                                                                                            return self.__width



                                                                                                            @width.setter

                                                                                                                def width(self, value):

                                                                                                                            if not isinstance(value, int):

                                                                                                                
