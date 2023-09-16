from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class inheriting from Rectangle

    Instance Attributes:
        width (int)
        height (int)
        x (int)
        y (int)

    Methods:
        area(self)
        display(self)
        update(self, *args, **kwargs)
    '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Getter and Setter for size'''
        return self.width

    @size.setter
    def size(self, new_size):
        setattr(self, 'width', new_size)
        setattr(self, 'height', new_size)

    def update(self, *args, **kwargs):
        '''Update Square attributes'''

        if args and len(args) > 0:
            i = 0
            attrs = ['id', 'size', 'x', 'y']

            for i in range(len(args)):
                setattr(self, attrs[i], args[i])

        elif kwargs:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def __str__(self):
        '''Return a Square definition'''

        printed = f"[Square] ({self.id}) {self.x}/{self.y} - "
        printed += f"{self.size}"
        return printed

    def to_dictionary(self):
        '''Return a dictionary description of the Square instance'''

        square_dict = {}

        square_dict['id'] = self.id
        square_dict['size'] = self.size
        square_dict['x'] = self.x
        square_dict['y'] = self.y

        return square_dict
