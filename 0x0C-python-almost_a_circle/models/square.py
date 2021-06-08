#!/usr/bin/python3
'''Almost a circle project'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Class that inherits Rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Instantiatior
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        Setting str representation
        '''
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)

    '''Getter'''
    @property
    def size(self):
        return self.width

    '''Setter'''
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    '''
    Public Methods
    '''
    def update(self, *args, **kwargs):
        '''
        that assigns attributes
        '''
        attrs = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for i in range(len(args)):
                if i == 1:
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''
        returns the dictionary representation
        of a Square instance
        '''
        attrs = ['id', 'size', 'x', 'y']
        new_dict = {}
        for key in attrs:
            if key == 'size':
                new_dict[key] = getattr(self, 'width')
            else:
                new_dict[key] = getattr(self, key)
        return new_dict
