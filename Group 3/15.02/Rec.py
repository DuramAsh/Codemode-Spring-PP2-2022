class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_per(self):
        return 2 * (self.length + self.width)

    def compare(self , r2): 
        if self.get_area() > r2.get_area():
            return f'First is bigger'
        else:
            return f'Second is bigger'
