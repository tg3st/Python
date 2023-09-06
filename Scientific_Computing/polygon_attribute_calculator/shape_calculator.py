class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return self.width*self.height
        
    def get_perimeter(self):
        self.perimeter = 2*self.width + 2*self.height
        return self.perimeter
        
    def get_diagonal(self):
        self.diagonal = (self.width**2 + self.height**2)**.5
        return self.diagonal
        
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ""
            for i in range(self.height):
              picture += "*"*self.width + "\n"
            return picture
        
    def get_amount_inside(self, shape):
        big_a = self.get_area()
        small_a = shape.get_area()
        n_inside = int(big_a/small_a)
        return n_inside

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

    def set_side(self, side):
        Rectangle.set_width(self, side)
        Rectangle.set_height(self, side)
    
    def __str__(self):
        return f"Square(side={self.width})"
