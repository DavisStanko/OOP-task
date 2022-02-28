#import other files
from shape_3D import Shape_3D
from cube import Cube
from ovoid import Ovoid

#colored text
#import Back to use background
from colorama import Fore

#Defualts
rgb = (0,0,0)

#Lists of options. The output is still hardcoded
options = ["Base", "Cube", "Ovoid"]
colors = ["Red", "Green", "Blue"]

#create and print the base shape
def display_base():
  global rgb
  base = Shape_3D("Base", rgb, """   _______
  |    |  |.-----.-----.-----.
  |       ||  _  |     |  -__|
  |__|____||_____|__|__|_____|""")
  base.print_type()
  base.print_color()
  base.print_art()
  print()

#create and print the cube
def display_cube():
  global rgb

  try:
    side = int(input("Please input the cube's side length: "))
  except:
    print("Invalid input! Please ONLY input numbers.\nMake sure NOT to put units (eg. mm, cm, in, ft)")
    display_cube()
  
  cube = Cube("Cube", rgb, """    +----+
   /    /|
  +----+ |
  |    | +
  |    |/
  +----+""", side)
  cube.print_type()
  cube.print_color()
  cube.print_art()
  cube.print_length()
  cube.print_volume()
  cube.print_surfacearea()
  print()

#create and print the ovoid
def display_ovoid():
  global rgb

  try:
    semi_Axis1 = int(input("Please input the ovoid's first semi-axis length: "))
  except:
    print("Invalid input! Please ONLY input numbers.\nMake sure NOT to put units (eg. mm, cm, in, ft)")
    display_ovoid()

  try:
    semi_Axis2 = int(input("Please input the ovoid's second semi-axis length: "))
  except:
    print("Invalid input! Please ONLY input numbers.\nMake sure NOT to put units (eg. mm, cm, in, ft)")
    display_ovoid()

  try:
    semi_Axis3 = int(input("Please input the ovoid's third semi-axis length: "))
  except:
    print("Invalid input! Please ONLY input numbers.\nMake sure NOT to put units (eg. mm, cm, in, ft)")
    display_ovoid()

  ovoid = Ovoid("Ovoid", rgb, """                                                                          
                          ░░▒▒██░░░░████████░░░░██▒▒▒▒                      
                    ░░░░▒▒▒▒▓▓░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓░░░░▒▒▒▒▒▒░░▒▒                
                ▒▒░░▒▒▒▒▒▒██▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▓▓░░▒▒▒▒░░▓▓            
              ▓▓  ▒▒▒▒▒▒██▒▒░░▓▓░░▓▓██▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒▓▓▒▒▒▒▒▒░░▓▓▒▒        
          ░░▓▓░░░░▒▒▒▒▒▒▓▓▒▒▒▒░░▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓░░░░▒▒▒▒▓▓▒▒▒▒▒▒  ▓▓▓▓      
        ▒▒██░░  ▒▒▒▒▒▒██▒▒░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░▒▒▓▓▒▒▒▒▒▒  ░░▓▓▓▓    
      ████▓▓░░▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓░░▒▒░░▒▒▓▓▒▒▒▒▒▒▒▒  ▒▒██▓▓  
    ▒▒▓▓▓▓░░░░▒▒▒▒▒▒▒▒▓▓▒▒░░▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓░░▒▒▒▒▓▓▒▒▒▒▒▒  ░░▓▓██  
    ▓▓▓▓▓▓░░░░▒▒▒▒▒▒▒▒▓▓░░░░▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓░░▒▒▒▒▓▓▒▒▒▒▒▒  ░░▓▓██░░
    ▓▓▓▓▓▓░░  ▒▒▒▒▒▒▓▓▒▒▒▒░░▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓██▒▒▒▒▒▒░░  ▓▓██▓▓
    ██▓▓▓▓  ░░▒▒░░▒▒▓▓▓▓▒▒░░▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒██▒▒▒▒▒▒░░░░▒▒████
    ██▓▓▓▓  ░░▒▒▒▒▒▒██▓▓▒▒▒▒▓▓░░▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▒▒░░▒▒▒▒██▒▒░░▒▒▒▒░░▒▒████
    ██▓▓▓▓  ░░▒▒░░▒▒▓▓▓▓▒▒▒▒▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒██▒▒▒▒▒▒░░░░▒▒████
    ▓▓▓▓▓▓░░  ▒▒▒▒▒▒▓▓▒▒▒▒░░▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓██▒▒▒▒▒▒░░  ▓▓██▓▓
    ▒▒▓▓██░░░░▒▒▒▒▒▒▒▒▓▓▒▒░░▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓░░▒▒▒▒▓▓▒▒▒▒▒▒  ░░▓▓██░░
      ▓▓██▓▓░░▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓░░▒▒░░▒▒▓▓▒▒▒▒▒▒▒▒  ▒▒██▓▓  
        ░░▓▓▒▒  ▒▒▒▒▒▒██▒▒░░▒▒░░▒▒▒▒▓▓▒▒▓▓▓▓▒▒▒▒░░░░░░▒▒▓▓▒▒▒▒▒▒  ░░██▓▓░░  
            ██░░░░▒▒▒▒▒▒▓▓▒▒▒▒░░██▓▓▒▒▒▒▒▒▒▒▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒░░  ▓▓▒▒      
              ▓▓░░▒▒▒▒▒▒▓▓▒▒░░▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒▓▓▒▒▒▒▒▒  ▓▓▒▒        
                ▒▒▒▒▒▒▒▒▒▒██▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▓▓▒▒▒▒▒▒░░▓▓░░          
                    ░░░░▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▓▓▒▒▒▒░░▒▒                
                            ░░▓▓▒▒░░▓▓████▓▓░░░░▓▓▒▒░░                      
  """, semi_Axis1, semi_Axis2, semi_Axis3)
  ovoid.print_type()
  ovoid.print_color()
  ovoid.print_art()
  ovoid.print_semiaxis1()
  ovoid.print_semiaxis2()
  ovoid.print_semiaxis3()
  ovoid.print_volume()
  ovoid.print_surfacearea()
  print()

  
def customize():
  global rgb
  # Print options from options list
  print("What color would you like the shape?")
  for i in range(len(options)):
      print(f"{i+1} : {colors[i]}")
    
  # Take user input and change color
  inp = input("Enter a number: ")
  if inp == "1":
    rgb = (255, 0, 0)
    print(Fore.RED)
  elif inp == "2":
    rgb = (0, 255, 0)
    print(Fore.GREEN)
  elif inp == "3":
    rgb = (0, 0, 255)
    print(Fore.BLUE)
  else:
    print("Invalid input! Please enter a listed number.")
    print()
    customize()

def prompt():
  #reset text to white + prompt
  #They're combined to avoid a blank line being printed
  print(Fore.WHITE + "What shape whould you like to display?")
  for i in range(len(options)):
      print(f"{i+1} : {options[i]}")
    
  # Take user input and run selected function
  inp = input("Enter a number: ")
  if inp == "1":
    print()
    customize()
    display_base()
    prompt()
  elif inp == "2":
    print()
    customize()
    display_cube()
    prompt()
  elif inp == "3":
    print()
    customize()
    display_ovoid()
    prompt()
  else:
    print()
    print("Invalid input! Please enter a listed number.")
    prompt()

prompt()