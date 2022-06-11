class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def set_width(self, newWidth):
       self.width = newWidth
       
       
    def set_height(self, newHeight):
        self.height = newHeight
        
        
    def get_area (self):
        return self.width * self.height
        
        
    def get_perimeter(self):
        return (self.height + self.width) * 2
        
        
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
        
        
    def get_picture(self):
        if self.width > 50 or self.height > 50 :
            return "Too big for picture."
            
        picture = ''
        i=0
        while i < self.height:
            j = 0
            while j < self.width:
                picture += '*'
                j += 1
            picture += '\n'
            i += 1
        
        return picture
        
    
    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)
        
    
    def get_amount_inside(self, shape):
        onWidth = self.width // shape.width
        onHeight = self.height // shape.height
        
        return onWidth * onHeight
        

class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side
        
    def set_width(self, newWidth):
       self.width = newWidth
       self.height = newWidth
       
       
    def set_height(self, newHeight):
        self.height = newHeight
        self.width = newHeight


    def set_side(self, side):
      self.height = side
      self.width = side
        
    
    def __str__(self):
        return 'Square(side={})'.format(self.width)

