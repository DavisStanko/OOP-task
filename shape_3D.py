class Shape_3D:
  def __init__(self, shape_Type, shape_Color, shape_Art):
    self.shape_Type = shape_Type
    self.shape_Color = shape_Color
    self.shape_Art = shape_Art
    
  def get_type(self):
    return self.shape_Type

  def get_color(self):
    return self.shape_Color

  def set_color(self, new_Color):
    self.shape_Color = new_Color
  
  def calc_volume(self):
    return 0

  def calc_surfacearea(self):
    return 0

  def print_type(self):
    print(f"Shape name = {self.shape_Type}")

  def print_color(self):
    print(f"RGB Color code = {self.shape_Color}")

  def print_art(self):
    print(self.shape_Art)

  