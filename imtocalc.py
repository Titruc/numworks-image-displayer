
from PIL import Image,ImageTk

def rgb_to_hex(r, g, b):


    # Convertir les valeurs RGB en hexadécimal
    hex_value = "{:02x}{:02x}{:02x}".format(r, g, b)
    return hex_value

def hex_to_rgb(hex_value):

    # Convertir la valeur hexadécimale en tuple RGB
    r = int(hex_value[0:2], 16)
    g = int(hex_value[2:4], 16)
    b = int(hex_value[4:6], 16)

    return r, g, b

def hex_to_base_custom(hex_string, custom_chars):
    binary_data = bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

   
    while len(binary_data) % 6 != 0:
        binary_data += '0'

    base_custom_data = ''
    for i in range(0, len(binary_data), 6):
        index = int(binary_data[i:i+6], 2)
        if 0 <= index < len(custom_chars):
            base_custom_data += custom_chars[index]
        else:
            raise ValueError("Index out of range in hex_to_base_custom")

   
    padding = len(binary_data) % 24
    if padding == 12:
        base_custom_data += '='
    elif padding == 18:
        base_custom_data += '=='

    return base_custom_data

def base_custom_to_hex(base_custom_string, custom_chars):
    base_custom_string = base_custom_string.rstrip('=')

    binary_data = ''
    for char in base_custom_string:
        index = custom_chars.find(char)
        if 0 <= index < len(custom_chars):
            binary_data += bin(index)[2:].zfill(6)
        else:
            raise ValueError("Character not found in custom_chars")

    hex_data = hex(int(binary_data, 2))[2:]

    if len(hex_data) % 2 != 0:
        hex_data = '0' + hex_data

    return hex_data


custom_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+=[]{}|;:'\",.<>?/\\~`"
hex_string = "3D9C49"
base_custom_string = hex_to_base_custom(hex_string, custom_chars)
print("Base custom:", base_custom_string)

hex_decoded = base_custom_to_hex(base_custom_string, custom_chars)
print("Hex décodé:", hex_decoded)

def hex_to_decimal(hex_string):
    # Ajouter des zéros à gauche pour assurer une longueur paire
    c = len(hex_string)
    if len(hex_string) < 7:
        hex_string = '0' + hex_string
    decimal_value = int(hex_string, 16)
    
    return decimal_value
def decimal_to_hexadecimal(decimal_number):
    
        # Utiliser la fonction hex() pour convertir en hexadécimal
        hexadecimal_representation = hex(decimal_number)
        return hexadecimal_representation
c = []
d=[]
im = Image.open(input("chemin d\'acces")) # lit l'image.
pix = im.load()
a=-1
b=-1
imsize = im.size  # prent la taille de l'image
print(imsize)
for i in range(imsize[1]):
    a=a+1
    b=0
    
    for j in range(imsize[0]):
        im2=im.getpixel((b,a))
        print(im2)
        if im2 != (0,0,0,0):
            c.append(hex_to_base_custom(rgb_to_hex(im2[0],im2[1],im2[2]),"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+=[]{}|;:'\",.<>?/\\~`"))
        else:
            c.append('')
        b=b+1
    d.append(c)
    c = []
        
with open('coucou.txt', 'w') as f:
    var = 'a'
    var2 = []
    for line in range(len(d)):
        var2.append(var+str(line))
        f.write("a"+str(line)+"="+str(tuple(d[line])))
        f.write('\n')
    v = str(var2[0])
    for i in var2[1:-1]:
        v = v+ ',' + str(i)
    v = v+ ','+str(var2[-1])
    f.write('image = ['+v+']')
        
        
        
        
    
