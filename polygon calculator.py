import math
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.width*self.height           
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    def get_diagonal(self):
        return math.sqrt(self.width**2+self.height**2)
    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        picture=""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture 
    def get_amount_inside(self,shape):
        fit_width=self.width//shape.width
        fit_height=self.height//shape.height
        return fit_width*fit_height
    def __str__(self):
        return f"Rectangle(width={self.width},height={self.height})"

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
    def set_width(self,side):
        self.width=side
        self.height=side
    def set_height(self,side):
        self.height=side
        self.width=side
    def set_side(self,side):
        self.width=side
        self.height=side        
    def __str__(self):
        return f"Square(side={self.width})"
    
rec=Rectangle(10,5)
print(rec.get_area())
print(rec.get_perimeter())
print(rec.get_diagonal()) #diagonal means the length of the line segment connecting two opposite corners of the rectangle
square=Square(10)
print(square.get_area())
print(square.get_perimeter())
print(square.get_diagonal())

