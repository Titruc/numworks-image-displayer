# Type your text here
from kandinsky import *

def base_custom_to_hex(base_custom_string, custom_chars):
    base_custom_string = base_custom_string.rstrip('=')

    binary_data = ''
    for char in base_custom_string:
        index = custom_chars.find(char)
        if 0 <= index < len(custom_chars):
            binary_representation = bin(index)[2:]
            binary_data += '0' * (6 - len(binary_representation)) + binary_representation
        else:
            raise ValueError("Character not found in custom_chars")

    hex_data = hex(int(binary_data, 2))[2:]

    if len(hex_data) % 2 != 0:
        hex_data = '0' + hex_data

    return hex_data

def hex_to_rgb(hex_value):
    """
    Return an RGB value of a hexadecimal color
    Parameter:
    - hex_value: Hexadecimal color value (Type: str)
    Return:
    - r, g, b: RGB values (Type: int)
    """
    # Ajouter des zéros à gauche si nécessaire
    hex_value = '0' * (6 - len(hex_value)) + hex_value

    r = int(hex_value[0:2], 16)
    g = int(hex_value[2:4], 16)
    b = int(hex_value[4:6], 16)

    return r, g, b
  
def display_image(image_list, pixel_size, image_size,x=0,y=0):
    """
    draw a pretty drawing UWU
    PARAMETERimage_list TYPE list, pixel_size TYPE int, image_size TYPE list
    RETURN None
    """
    index = 0
    nbr_pixel = 0
    pixel_list = image_list[index]
    for i in range(image_size[1]):
        fill_rect(0,i*pixel_size+y*pixel_size,320,pixel_size,(255,255,255))
        for j in range(image_size[0]):
            color = pixel_list
            if pixel_list[nbr_pixel] != '':
              fill_rect(j*pixel_size+x*pixel_size,i*pixel_size+y*pixel_size,pixel_size,pixel_size, hex_to_rgb(str(base_custom_to_hex(pixel_list[nbr_pixel],"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+=[]{}|;:'\",.<>?/\\~`"))))
            else:
              pass
            if nbr_pixel < len(pixel_list):
                nbr_pixel+=1
            else:
                nbr_pixel = 0
        nbr_pixel = 0
        
        try:
            pixel_list = image_list[index]
        except:
            pass
        index+=1
            
    return None





from avocado import *
display_image(image,11,[32,22],0,5)
 #display_image(image,11,[32,22],0,10)

