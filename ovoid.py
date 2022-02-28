#import base class
from shape_3D import Shape_3D

class Ovoid(Shape_3D):
  def __init__(self, shape_Type, shape_Color, shape_Art, semi_Axis1, semi_Axis2, semi_Axis3):
    self.shape_Type = shape_Type
    self.shape_Color = shape_Color
    self.shape_Art = shape_Art
    self.semi_Axis1 = semi_Axis1
    self.semi_Axis2 = semi_Axis2
    self.semi_Axis3 = semi_Axis3

  def get_type(self):
    return self.shape_Type

  def get_color(self):
    return self.shape_Color

  def set_color(self, new_Color):
    self.shape_Color = new_Color

  def calc_volume(self):
    return round((4/3 * 3.141592653589793 * self.semi_Axis1 * self.semi_Axis2 * self.semi_Axis3), 2)

  def calc_surfacearea(self):
    ab = ((self.semi_Axis1 * self.semi_Axis2) ** 1.6)
    ac = ((self.semi_Axis1 * self.semi_Axis3) ** 1.6)
    bc = ((self.semi_Axis2 * self.semi_Axis2) ** 1.6)
    return round((4 * 3.141592653589793 * (((ab+ac+bc)/3) ** (1/1.6))), 2)

  def print_type(self):
    print(f"Shape name = {self.shape_Type}")

  def print_color(self):
    print(f"RGB Color code = {self.shape_Color}")

  def print_art(self):
    print(self.shape_Art)

  def print_semiaxis1(self):
    print(f"Side1 = {self.semi_Axis1}units")

  def print_semiaxis2(self):
    print(f"Side2 = {self.semi_Axis2}units")

  def print_semiaxis3(self):
    print(f"Side3 = {self.semi_Axis3}units")
  
  def print_volume(self):
    print(f"Volume = {self.calc_volume()}units")

  def print_surfacearea(self):
    print(f"Surface Area = {self.calc_surfacearea()}units")