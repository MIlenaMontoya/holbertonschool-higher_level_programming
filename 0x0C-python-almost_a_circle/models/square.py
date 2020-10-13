#!/usr/bin/python3
"""[summary]
    """
# task 10
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

# task 11
    @property
    def size(self):
            return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

# task 12
    def update(self, *args, **kwargs):

# task 14
    def to_dictionary(self):
        self.id
        self.size
        self.x
        self.y
    
    
