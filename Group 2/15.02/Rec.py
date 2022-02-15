class Rectangle:
    
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def compare_by_area(self, Rec):
        if self.get_area() > Rec.get_area():
            return self.get_area()
        else:
            return Rec.get_area()