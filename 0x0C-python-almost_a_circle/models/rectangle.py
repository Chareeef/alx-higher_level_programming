from models.base import Base


class Rectangle(Base):
    '''A Rectangle class

    Instance Attributes:
        width (int)
        height (int)
        x (int)
        y (int)
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        '''Getter and Setter for width'''
        return self.__width

    @width.setter
    def width(self, new_width):
        if type(new_width) is not int:
            raise TypeError('width must be an integer')
        elif new_width <= 0:
            raise ValueError('width must be > 0')

        self.__width = new_width

    @property
    def height(self):
        '''Getter and Setter for height'''
        return self.__height

    @height.setter
    def height(self, new_height):
        if type(new_height) is not int:
            raise TypeError('height must be an integer')
        elif new_height <= 0:
            raise ValueError('height must be > 0')

        self.__height = new_height

    @property
    def x(self):
        '''Getter and Setter for x'''
        return self.__x

    @x.setter
    def x(self, new_x):
        if type(new_x) is not int:
            raise TypeError('x must be an integer')
        elif new_x < 0:
            raise ValueError('x must be >= 0')

        self.__x = new_x

    @property
    def y(self):
        '''Getter and Setter for y'''
        return self.__y

    @y.setter
    def y(self, new_y):
        if type(new_y) is not int:
            raise TypeError('y must be an integer')
        elif new_y < 0:
            raise ValueError('y must be >= 0')

        self.__y = new_y

    def area(self):
        '''Return the rectangle's area'''

        return self.height * self.width

    def display(self):
        '''Display the rectangle using `#` symbol'''

        rect_repr = ''

        rect_repr += '\n' * self.y

        for h in range(self.height):
            rect_repr += ' ' * self.x
            for w in range(self.width):
                rect_repr += '#'
            if h < self.height - 1:
                rect_repr += '\n'

        print(rect_repr)

    def __str__(self):
        '''Return a Rectangle definition'''

        printed = f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
        printed += f"{self.width}/{self.height}"
        return printed
