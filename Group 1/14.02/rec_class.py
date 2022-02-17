class Rectangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def change_color(self, color):
        self.color = color

    def compare_areas(self, R):
        if self.get_area() > R.get_area():
            return self.get_area()
        else:
            return R.get_area()