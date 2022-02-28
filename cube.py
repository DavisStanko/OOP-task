#import base class
from shape_3D import Shape_3D

class Cube(Shape_3D):
  def __init__(self, shape_Type, shape_Color, shape_Art, side_Length):
    self.shape_Type = shape_Type
    self.shape_Color = shape_Color
    self.shape_Art = shape_Art
    self.side_Length = side_Length

  def get_type(self):
    return self.shape_Type

  def get_color(self):
    return self.shape_Color

  def set_color(self, new_Color):
    self.shape_Color = new_Color

  def calc_volume(self):
    return round((self.side_Length**3), 2)

  def calc_surfacearea(self):
    return round((6*(self.side_Length**2)), 2)

  def print_type(self):
    print(f"Shape name = {self.shape_Type}")

  def print_color(self):
    print(f"RGB Color code = {self.shape_Color}")

  def print_art(self):
    print(self.shape_Art)

  def print_length(self):
    print(f"Side = {self.side_Length}units")
  
  def print_volume(self):
    print(f"Volume = {self.calc_volume()}units")

  def print_surfacearea(self):
    print(f"Surface Area = {self.calc_surfacearea()}units")